from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("copyright", "Авторские права"),
            types.BotCommand("sites", "Сайты"),
            types.BotCommand("shedule", "Расписание"),
        ]
    )
