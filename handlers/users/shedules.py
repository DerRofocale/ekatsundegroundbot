import asyncio
import datetime
from datetime import date
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.dbutils import AddNewUser
from keyboards.default.startdefkey import startkeyboard, stationskeyboard, towherekeyboard
from keyboards.inline.sheduleinlkey import shedulekeyboard
from keyboards.inline.sitesinlkey import siteskeyboard
from loader import dp, bot
from bdateutil import isbday
from aiogram.dispatcher.filters import Command, Text, state
from aiogram.dispatcher import FSMContext

from media.drawimage import DrawTime
from media.getimage import GetImage
from shedules.weekdaysfrom1to9 import fromst1tost9weekday
from states.soontrainstates import SoonTrain


@dp.message_handler(text="Ближайший поезд", state=None)
async def exts(message: types.Message):
    text = [
        "Пожалуйста, выберите станцию",
    ]
    await message.answer("\n".join(text), reply_markup=stationskeyboard, parse_mode=types.ParseMode.HTML)
    await SoonTrain.TakeStation.set()


#######################################################################################################################
@dp.message_handler(text="Проспект Космонавтов", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(photo=await DrawTime(1, 9), reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Уралмаш", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)

    await state.update_data(FromStation=2)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Машиностроителей", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    await state.update_data(FromStation=3)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Уральская", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    await state.update_data(FromStation=4)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Динамо", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    await state.update_data(FromStation=5)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Площадь 1905 года", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    await state.update_data(FromStation=6)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Геологическая", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    await state.update_data(FromStation=7)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Чкаловская", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    await state.update_data(FromStation=8)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Ботаническая", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(photo=await DrawTime(9, 1), reply_markup=startkeyboard)
    await state.finish()


#######################################################################################################################
@dp.message_handler(text="Проспект Космонавтов", state=SoonTrain.TakeToWhere)
async def exts(message: types.Message, state: FSMContext):
    data = await state.get_data()
    FRMST = data.get("FromStation")
    await message.answer_photo(photo=await DrawTime(FRMST, 1), reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Ботаническая", state=SoonTrain.TakeToWhere)
async def exts(message: types.Message, state: FSMContext):
    data = await state.get_data()
    FRMST = data.get("FromStation")
    await message.answer_photo(photo=await DrawTime(FRMST, 9), reply_markup=startkeyboard)
    await state.finish()


#######################################################################################################################
