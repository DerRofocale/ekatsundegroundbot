from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.startdefkey import startkeyboard, stationskeyboard
from keyboards.inline.sheduleinlkey import shedulekeyboard
from loader import dp, bot
from media.strings import IMGYanDiskSheme1, IMGYanDiskSheme2, IMGYanDiskSheme3, IMGYanDiskSheme4, IMGYanDiskSheme5, \
    IMGYanDiskSheme6, IMGYanDiskSheme7, IMGYanDiskSheme8, IMGYanDiskSheme9
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
    await message.answer_photo(IMGYanDiskSheme1, reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Уралмаш", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(IMGYanDiskSheme2, reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Машиностроителей", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(IMGYanDiskSheme3, reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Уральская", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(IMGYanDiskSheme4, reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Динамо", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(IMGYanDiskSheme5, reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Площадь 1905 года", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(IMGYanDiskSheme6, reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Геологическая", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(IMGYanDiskSheme7, reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Чкаловская", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(IMGYanDiskSheme8, reply_markup=startkeyboard)
    await state.finish()


@dp.message_handler(text="Ботаническая", state=ExitsFromStation.TakeStation)
async def exts(message: types.Message, state: FSMContext):
    await message.answer_photo(IMGYanDiskSheme9, reply_markup=startkeyboard)
    await state.finish()
