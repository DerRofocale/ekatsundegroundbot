from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.startdefkey import startkeyboard, stationskeyboard
from keyboards.inline.sheduleinlkey import shedulekeyboard
from loader import dp, bot
from states.exitsfromstationstates import ExitsFromStation
from media.getimage import GetImage


@dp.message_handler(text="Схема выходов", state=None)
async def exts(message: types.Message):
    text = [
        "Пожалуйста, выберите станцию",
    ]
    await message.answer("\n".join(text), reply_markup=stationskeyboard, parse_mode=types.ParseMode.HTML)
    await ExitsFromStation.TakeStation.set()


@dp.message_handler(text="Проспект Космонавтов", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(await GetImage("shemaexits/1-1.jpg"), reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Уралмаш", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(await GetImage("shemaexits/2-1.jpg"), reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Машиностроителей", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(await GetImage("shemaexits/3-1.jpg"), reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Уральская", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(await GetImage("shemaexits/4-1.jpg"), reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Динамо", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(await GetImage("shemaexits/5-1.jpg"), reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Площадь 1905 года", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(await GetImage("shemaexits/6-1.jpg"), reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Геологическая", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(await GetImage("shemaexits/7-1.jpg"), reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Чкаловская", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(await GetImage("shemaexits/8-1.jpg"), reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Ботаническая", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(await GetImage("shemaexits/9-1.jpg"), reply_markup=startkeyboard)
    await state.finish()
