from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


startkeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Когда следующий поезд?"),
        ]
    ],
    resize_keyboard=True
)