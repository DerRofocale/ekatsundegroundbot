from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


shedulekeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Актуальное расписание", url="https://metro-ektb.ru/podrobnye-grafiki-po-stanciyam/")
        ]
    ]
)
