from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Запустить бота",
            "/copyright - Авторские права",
            "/sites - Сайты",
            "/shedule - Расписание")
    await message.answer("\n".join(text))
