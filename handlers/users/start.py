import asyncio
import datetime
from datetime import date
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.dbutils import AddNewUser
from keyboards.default.startdefkey import startkeyboard
from keyboards.inline.sheduleinlkey import shedulekeyboard
from keyboards.inline.sitesinlkey import siteskeyboard
from loader import dp, bot
from bdateutil import isbday
from aiogram.dispatcher.filters import Command, Text, state
from aiogram.dispatcher import FSMContext
from media.getimage import GetImage
from media.strings import IMGYanDiskLogo
from shedules.weekdaysfrom1to9 import fromst1tost9weekday
from states.exitsfromstationstates import ExitsFromStation
from states.soontrainstates import SoonTrain


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await AddNewUser(message.chat.id, message.chat.first_name)
    text = [
        f"Привет, {message.chat.first_name}! 👋🏻",
        f"",
        "Данный бот покажет тебе сколько времени осталось до прибытия ближайшего состава на твою станцию",
        "",
        "Пользуйзя кнопками снизу 👇🏻",
        "Если нужна дополнительная информация, пиши /help"
    ]
    await message.answer_photo(IMGYanDiskLogo, "\n".join(text),
                               parse_mode=types.ParseMode.HTML, reply_markup=startkeyboard)


@dp.message_handler(commands=['copyright'])
async def cmnd(message: types.Message):
    text = [
        f"Мы не являемся владельцами и не заявляем авторские права на цифровую и/или интеллектуальную собственность "
        f"материалов, использованых в данном боте.",
        f"Все материалы и информация взяты из открытых интернет-источников.",
        "Данный бот покажет тебе сколько времени осталось до прибытия ближайшего состава на твою станцию",
        "",
        "<b>Федеральный закон от 27.07.2006 N 149-ФЗ (ред. от 30.12.2021) \"Об информации, информационных технологиях "
        "и о защите информации\" (с изм. и доп., вступ. в силу с 01.01.2022)</b>",
        "Статья 7. Общедоступная информация",
        "1. К общедоступной информации относятся общеизвестные сведения и иная информация, доступ к которой не "
        "ограничен.",
        "2. Общедоступная информация может использоваться любыми лицами по их усмотрению при соблюдении установленных "
        "федеральными законами ограничений в отношении распространения такой информации.",
        "3. Обладатель информации, ставшей общедоступной по его решению, вправе требовать от лиц, распространяющих "
        "такую информацию, указывать себя в качестве источника такой информации.",
        "",
        "Если Вы являетесь правообладателем инфомации или материалов, которые использованы в боте, и Вы хотите, "
        "чтобы мы указали Ваше авторство, пожалуйста, напишите об этом @dmitry_yalchik.",
        "",
        "<b>Сервис предоставляется исключительно в информационно-демонстрационных целях по принципу “как есть” (“as is”).</b>"
    ]
    await message.answer("\n".join(text), parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands=['sites'])
async def cmnd(message: types.Message):
    await message.answer("<b>Официальный сайт метрополитена и сайты партнёров:</b>", reply_markup=siteskeyboard, parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands=['shedule'])
async def cmnd(message: types.Message):
    text = [
        f"График, отображаемый в боте соответствует графику по станциям с официального сайта Екатеринбургского метрополитена.",
        f"",
        f"Актуальность данных: 13.04.2022 год",
    ]
    await message.answer("\n".join(text), reply_markup=shedulekeyboard, parse_mode=types.ParseMode.HTML)








# @dp.message_handler(state=ADMPNL.AddNewAdmin1)
# async def AddNewAdminMethod(message: types.Message, state: FSMContext):
#     if message.text.isdigit():
#         await state.update_data(IDNewAdmin=message.text)  # внесение имени в хранилище
#         await message.answer("Укажите имя нового администратора")
#         await ADMPNL.AddNewAdmin2.set()
#     else:
#         await message.answer("Некорректный Telegram ID.\nПопробуйте ещё раз.\nОн должен состоять только из цифр.")