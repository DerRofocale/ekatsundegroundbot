from aiogram import types
from aiogram.dispatcher import FSMContext
from database import GetAllAdmins
from database.createtable import CreateTableUsers, CreateTableAdmins, CreateTableStats
from database.dbutils import AddNewAdmin, DeleteAdmin, GetAllUsers
from keyboards.default.admin import adminmenu, returnAdminPanel, spamChoise, adminYesOrNo
from loader import dp, bot
from states.adminstate import ADMPNL


@dp.message_handler(commands=['admin'])
async def ClearState(message: types.Message):
    ADM = await GetAllAdmins()
    for admin in ADM:
        if admin[0] == message.chat.id:
            await ADMPNL.ADMIN.set()
            await message.answer("Вы вошли в панель администрирования ботом!", reply_markup=adminmenu)


@dp.message_handler(text="Главное меню", state=ADMPNL)
async def GetOutAdminPanel(message: types.Message, state: FSMContext):
    await state.finish()
    await ADMPNL.ADMIN.set()
    await message.answer("Вы вернулись в главное меню панели администрирования ботом", reply_markup=adminmenu)


@dp.message_handler(text="Список пользователей", state=ADMPNL)
async def cmnd(message: types.Message):
    try:
        await message.answer_document(await CreateTableUsers())
    except Exception as err:
        print(err)


@dp.message_handler(text="Статистика использования", state=ADMPNL)
async def cmnd(message: types.Message):
    try:
        await message.answer_document(await CreateTableStats())
    except Exception as err:
        print(err)


@dp.message_handler(text="Список админов", state=ADMPNL)
async def cmnd(message: types.Message):
    try:
        await message.answer_document(await CreateTableAdmins())
    except Exception as err:
        print(err)


@dp.message_handler(text="Выйти из админ-панели", state=ADMPNL)
async def GetOutAdminPanel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Вы вышли из админ-панели", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(text="Добавить админа", state=ADMPNL)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    await ADMPNL.AddNewAdmin1.set()
    text = [
        "Введите Telegram ID человека, которого хотите назначить админом.",
        "Пожалуйста, проверьте точность вводимых данны.",
        "",
        "Чтобы получить ID добавляемого человека, необходимо с его устройства отправить в данного бота команду /getmyid",
    ]
    await message.answer("\n".join(text), reply_markup=returnAdminPanel)


@dp.message_handler(state=ADMPNL.AddNewAdmin1)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(IDNewAdmin=message.text)  # внесение имени в хранилище
        await message.answer("Укажите имя нового администратора")
        await ADMPNL.AddNewAdmin2.set()
    else:
        await message.answer("Некорректный Telegram ID.\nПопробуйте ещё раз.\nОн должен состоять только из цифр.")


@dp.message_handler(state=ADMPNL.AddNewAdmin2)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    data = await state.get_data()
    IDTG = data.get("IDNewAdmin")
    await message.answer(f"{IDTG} - {message.text}")
    await AddNewAdmin(IDTG, message.text)
    try:
        await dp.bot.send_message(IDTG, "Вам назначили роль админа!")
    except Exception:
        pass
    await ADMPNL.ADMIN.set()
    await message.answer(f"Администратор c ID <code>{IDTG}</code> успешно добавлен!", reply_markup=adminmenu, parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Удалить админа", state=ADMPNL)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    await ADMPNL.DeleteAdmin1.set()
    text = [
        "Введите Telegram ID человека, с которого хотите снять полномочия админа.",
        "Пожалуйста, проверьте точность вводимых данны.",
        "",
        "Чтобы получить ID добавляемого человека, необходимо с его устройства отправить в данного бота команду\n/getmyid",
    ]
    await message.answer("\n".join(text), reply_markup=returnAdminPanel)


@dp.message_handler(content_types=types.ContentType.TEXT, state=ADMPNL.DeleteAdmin1)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        if await DeleteAdmin(message.text) == True:
            await message.answer(f"Администратор с ID <code>{message.text}</code> успешно удалён!", reply_markup=adminmenu, parse_mode=types.ParseMode.HTML)
            if str(message.from_user.id) != message.text:
                try:
                    await dp.bot.send_message(message.text, "С Вас сняли полномочия админа!")
                except Exception:
                    pass
                await ADMPNL.ADMIN.set()
            else:
                await dp.bot.send_message(message.text, "Вы сняли с себя полномочия администратора!", reply_markup=types.ReplyKeyboardRemove())
                await state.finish()
        else:
            await message.answer("Администратор не удалён!\nПожалуйста, проверьте правильность введённого ID.")
    else:
        await message.answer("Некорректный Telegram ID.\nПопробуйте ещё раз.\nОн должен состоять только из цифр.")


@dp.message_handler(text="Рассылка", state=ADMPNL)
async def GetOutAdminPanel(message: types.Message, state: FSMContext):
    await message.answer("Выберите тип рыссылки", reply_markup=spamChoise)
    await ADMPNL.SPAM.set()


@dp.message_handler(text="Текст", state=ADMPNL.SPAM)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    text = [
        "Пришлите текст, который необходимо разослать."
    ]
    await message.answer("\n".join(text), reply_markup=returnAdminPanel)
    await ADMPNL.SPAMText.set()


@dp.message_handler(content_types=types.ContentType.TEXT, state=ADMPNL.SPAMText)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    await state.update_data(SPAMText=message.text)  # внесение имени в хранилище
    await ADMPNL.SPAMYesOrNoText.set()
    await message.answer("<b>Предварительный просмотр:</b>", parse_mode=types.ParseMode.HTML)
    await message.answer(message.text)
    await message.answer("Подтвердите рассылку:", reply_markup=adminYesOrNo)

@dp.message_handler(content_types=types.ContentType.TEXT, state=ADMPNL.SPAMYesOrNoText)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    if message.text == "Да":
        data = await state.get_data()
        SPAMText = data.get("SPAMText")
        await message.answer("Рассылка начата!", reply_markup=adminmenu)
        await state.finish()
        await ADMPNL.ADMIN.set()
        USS = await GetAllUsers()
        for user in USS:
            try:
                await dp.bot.send_message(user[0], SPAMText)
            except Exception as err:
                pass
    if message.text == "Нет":
        await message.answer("Рассылка отменена!", reply_markup=adminmenu)
        await state.finish()
        await ADMPNL.ADMIN.set()


@dp.message_handler(text="Фото", state=ADMPNL.SPAM)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    text = [
        "Пришлите одно фото, которое необходимо разослать."
    ]
    await message.answer("\n".join(text), reply_markup=returnAdminPanel)
    await ADMPNL.SPAMPhoto.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=ADMPNL.SPAMPhoto)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    await state.update_data(SPAMPhoto=message.photo[-1].file_id)  # внесение имени в хранилище
    await ADMPNL.SPAMYesOrNoPhoto.set()
    await message.answer("<b>Предварительный просмотр:</b>", parse_mode=types.ParseMode.HTML)
    await message.answer_photo(message.photo[-1].file_id)
    await message.answer("Подтвердите рассылку:", reply_markup=adminYesOrNo)


@dp.message_handler(content_types=types.ContentType.TEXT, state=ADMPNL.SPAMYesOrNoPhoto)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    if message.text == "Да":
        data = await state.get_data()
        SPAMPhoto = data.get("SPAMPhoto")
        await message.answer("Рассылка начата!", reply_markup=adminmenu)
        await state.finish()
        await ADMPNL.ADMIN.set()
        USS1 = await GetAllUsers()
        for user1 in USS1:
            try:
                await bot.send_photo(user1[0], SPAMPhoto)
            except Exception as err:
                print(err)
    if message.text == "Нет":
        await message.answer("Рассылка отменена!", reply_markup=adminmenu)
        await state.finish()
        await ADMPNL.ADMIN.set()


@dp.message_handler(text="Текст + фото", state=ADMPNL.SPAM)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    text = [
        "Пришлите одно фото."
    ]
    await message.answer("\n".join(text), reply_markup=returnAdminPanel)
    await ADMPNL.SPAMTextAndPhoto1.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=ADMPNL.SPAMTextAndPhoto1)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    await state.update_data(SPAMTextAndPhotoIMG=message.photo[-1].file_id)  # внесение имени в хранилище
    await ADMPNL.SPAMTextAndPhoto2.set()
    await message.answer("Пришлите текст, который необходимо прикрепить к фотографии.")


@dp.message_handler(content_types=types.ContentType.TEXT, state=ADMPNL.SPAMTextAndPhoto2)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    await state.update_data(SPAMTextAndPhotoTXT=message.text)  # внесение имени в хранилище
    await ADMPNL.SPAMYesOrNoTextAndPhoto.set()
    data = await state.get_data()
    SPAMPhot = data.get("SPAMTextAndPhotoIMG")
    await message.answer("<b>Предварительный просмотр:</b>", parse_mode=types.ParseMode.HTML)
    await message.answer_photo(SPAMPhot, message.text)
    await message.answer("Подтвердите рассылку:", reply_markup=adminYesOrNo)



@dp.message_handler(content_types=types.ContentType.TEXT, state=ADMPNL.SPAMYesOrNoTextAndPhoto)
async def AddNewAdminMethod(message: types.Message, state: FSMContext):
    if message.text == "Да":
        data = await state.get_data()
        SPAMPh = data.get("SPAMTextAndPhotoIMG")
        SPAMTx = data.get("SPAMTextAndPhotoTXT")
        await message.answer("Рассылка начата!", reply_markup=adminmenu)
        await state.finish()
        await ADMPNL.ADMIN.set()
        USS2 = await GetAllUsers()
        for user2 in USS2:
            try:
                await bot.send_photo(user2[0], SPAMPh, SPAMTx)
            except Exception as err:
                print(err)
    if message.text == "Нет":
        await message.answer("Рассылка отменена!", reply_markup=adminmenu)
        await state.finish()
        await ADMPNL.ADMIN.set()
