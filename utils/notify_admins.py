import logging
from aiogram import Dispatcher
from database import GetAllAdmins
from aiogram import types


async def on_startup_notify(dp: Dispatcher):
    ADM = await GetAllAdmins()
    for admin in ADM:
        try:
            await dp.bot.send_message(admin[0], "Бот запущен!", disable_notification=True)
        except Exception as err:
            logging.exception(err)
