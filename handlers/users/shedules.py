import asyncio
import datetime
from contextlib import suppress
from datetime import date
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

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

async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()



@dp.message_handler(text="Ближайший поезд", state=None)
async def exts(message: types.Message, state: FSMContext):
    text = [
        "Пожалуйста, выберите станцию",
    ]
    msg = await message.answer("\n".join(text), reply_markup=stationskeyboard, parse_mode=types.ParseMode.HTML)
    await SoonTrain.TakeStation.set()
    await asyncio.create_task(delete_message(message, 0))
    await state.update_data(MessageForDelete=msg)

#######################################################################################################################
@dp.message_handler(text="Проспект Космонавтов", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    imgmsg = await message.answer_photo(photo=await DrawTime(1, 9), caption="Изображение будет удалено через 10 минут", reply_markup=startkeyboard)
    data = await state.get_data()
    MFD = data.get("MessageForDelete")
    await asyncio.create_task(delete_message(MFD, 0))
    await asyncio.create_task(delete_message(message, 0))
    await state.finish()
    await asyncio.create_task(delete_message(imgmsg, 600))

@dp.message_handler(text="Уралмаш", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    msg = await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    data = await state.get_data()
    MFD = data.get("MessageForDelete")
    await asyncio.create_task(delete_message(MFD, 0))
    await state.update_data(MessageForDeleteTwo=msg)
    await asyncio.create_task(delete_message(message, 0))
    await state.update_data(FromStation=2)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Машиностроителей", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    msg = await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    data = await state.get_data()
    MFD = data.get("MessageForDelete")
    await asyncio.create_task(delete_message(MFD, 0))
    await state.update_data(MessageForDeleteTwo=msg)
    await asyncio.create_task(delete_message(message, 0))
    await state.update_data(FromStation=3)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Уральская", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    msg = await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    data = await state.get_data()
    MFD = data.get("MessageForDelete")
    await asyncio.create_task(delete_message(MFD, 0))
    await state.update_data(MessageForDeleteTwo=msg)
    await asyncio.create_task(delete_message(message, 0))
    await state.update_data(FromStation=4)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Динамо", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    msg = await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    data = await state.get_data()
    MFD = data.get("MessageForDelete")
    await asyncio.create_task(delete_message(MFD, 0))
    await state.update_data(MessageForDeleteTwo=msg)
    await asyncio.create_task(delete_message(message, 0))
    await state.update_data(FromStation=5)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Площадь 1905 года", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    msg = await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    data = await state.get_data()
    MFD = data.get("MessageForDelete")
    await asyncio.create_task(delete_message(MFD, 0))
    await state.update_data(MessageForDeleteTwo=msg)
    await asyncio.create_task(delete_message(message, 0))
    await state.update_data(FromStation=6)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Геологическая", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    msg = await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    data = await state.get_data()
    MFD = data.get("MessageForDelete")
    await asyncio.create_task(delete_message(MFD, 0))
    await state.update_data(MessageForDeleteTwo=msg)
    await asyncio.create_task(delete_message(message, 0))
    await state.update_data(FromStation=7)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Чкаловская", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    msg = await message.answer("Пожалуйста, выберите направление", reply_markup=towherekeyboard)
    data = await state.get_data()
    MFD = data.get("MessageForDelete")
    await asyncio.create_task(delete_message(MFD, 0))
    await state.update_data(MessageForDeleteTwo=msg)
    await asyncio.create_task(delete_message(message, 0))
    await state.update_data(FromStation=8)
    await SoonTrain.TakeToWhere.set()


@dp.message_handler(text="Ботаническая", state=SoonTrain.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    imgmsg = await message.answer_photo(photo=await DrawTime(9, 1), caption="Изображение будет удалено через 10 минут", reply_markup=startkeyboard)
    data = await state.get_data()
    MFD = data.get("MessageForDelete")
    await asyncio.create_task(delete_message(MFD, 0))
    await asyncio.create_task(delete_message(message, 0))
    await state.finish()
    await asyncio.create_task(delete_message(imgmsg, 600))



#######################################################################################################################
@dp.message_handler(text="Проспект Космонавтов", state=SoonTrain.TakeToWhere)
async def exts(message: types.Message, state: FSMContext):
    data = await state.get_data()
    FRMST = data.get("FromStation")
    MFD = data.get("MessageForDeleteTwo")
    await asyncio.create_task(delete_message(MFD, 0))
    await asyncio.create_task(delete_message(message, 0))
    imgmsg = await message.answer_photo(photo=await DrawTime(FRMST, 1), caption="Изображение будет удалено через 10 минут", reply_markup=startkeyboard)
    await state.finish()
    await asyncio.create_task(delete_message(imgmsg, 600))


@dp.message_handler(text="Ботаническая", state=SoonTrain.TakeToWhere)
async def exts(message: types.Message, state: FSMContext):
    data = await state.get_data()
    FRMST = data.get("FromStation")
    MFD = data.get("MessageForDeleteTwo")
    await asyncio.create_task(delete_message(MFD, 0))
    await asyncio.create_task(delete_message(message, 0))
    imgmsg = await message.answer_photo(photo=await DrawTime(FRMST, 9), caption="Изображение будет удалено через 10 минут", reply_markup=startkeyboard)
    await state.finish()
    await asyncio.create_task(delete_message(imgmsg, 600))


#######################################################################################################################
