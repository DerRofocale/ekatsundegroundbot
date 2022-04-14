import asyncio
import datetime
from datetime import date
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.dbutils import AddNewUser
from keyboards.default.start import startkeyboard
from loader import dp, bot
from bdateutil import isbday
from aiogram.dispatcher.filters import Command, Text, state
from aiogram.dispatcher import FSMContext


    #date.isoweekday()


from media.getimage import DrawTime, GetImage
from shedules.weekdaysfrom1to9 import fromst1tost9weekday


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await AddNewUser(message.chat.id, message.chat.first_name)
    val = isbday(date.today())
    if val:
        await message.answer("Привет! Сегодня будний день.", reply_markup=startkeyboard)
    else:
        await message.answer("Привет! Сегодня выходной день.", reply_markup=startkeyboard)

@dp.message_handler(text="Когда следующий поезд?")
async def getmenu(message: types.Message):
    if datetime.time(0, 0) < datetime.datetime.now().time() < datetime.time(6, 00): # СМОТРИМ ТОЛЬКО НОЧЬ ПРЕДЫДУЩЕГО ДНЯ
        if datetime.datetime.today().isoweekday() == 1:
            print("1 Смотрим на ВЫХОДНОЙ")
            await message.answer("1 ")
        elif datetime.datetime.today().isoweekday() == 2:
            print("2 Смотрим на БУДНИЙ")
            await message.answer("2 ")
        elif datetime.datetime.today().isoweekday() == 4:
            print("3 Смотрим на БУДНИЙ")
            await message.answer("3 ")

            for admin in fromst1tost9weekday:
                if admin > datetime.datetime.now().time() > datetime.time(0, 30):
                    print(f"{admin.hour}:{admin.minute}:{admin.second}")
                    now = datetime.datetime(year=2022, month=4, day=13, hour=admin.hour, minute=admin.minute, second=admin.second)
                    till_ten_hours_fifteen_minutes = now - datetime.timedelta(hours=datetime.datetime.now().hour, minutes=datetime.datetime.now().minute, seconds=datetime.datetime.now().second)
                    print(till_ten_hours_fifteen_minutes)
                    text = [
                        "<code>Станция отправления:</code> Уралмаш",
                        "<code>В сторону станции:</code> Проспект Космонавтов",
                        "",
                        f"<code>До прибытия поезда:</code> {till_ten_hours_fifteen_minutes.minute} МИН {till_ten_hours_fifteen_minutes.second} С",
                    ]
                    await message.answer_photo(await DrawTime(till_ten_hours_fifteen_minutes), "\n".join(text), parse_mode=types.ParseMode.HTML)
                    break


                # elif datetime.time(0, 0) < datetime.datetime.now().time() < datetime.time(0, 30):
                #     if datetime.time(0, 0) < admin < datetime.time(0, 30):
                #         print("qwe")
                #         print(f"{admin.hour}:{admin.minute}:{admin.second}")
                elif admin is fromst1tost9weekday[-1]:
                    await message.answer_photo(await GetImage("closed.jpg"), f"Все станции метрополитена уже закрыты.")





        elif datetime.datetime.today().isoweekday() == 4:
            print("4 Смотрим на БУДНИЙ")
            await message.answer("4 ")
        elif datetime.datetime.today().isoweekday() == 5:
            print("5 Смотрим на БУДНИЙ")
            await message.answer("5 ")
        elif datetime.datetime.today().isoweekday() == 6:
            print("6 Смотрим на БУДНИЙ")
            await message.answer("6 ")
        elif datetime.datetime.today().isoweekday() == 7:
            print("7 Смотрим на ВЫХОДНОЙ")
            await message.answer("7")
    else: # СМОТРИМ СЕГОДНЯШНИЙ ДЕНЬ
        print("Метро не работает")
        await message.answer("Метро не работает")