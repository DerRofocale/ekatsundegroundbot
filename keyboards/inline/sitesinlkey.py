from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


siteskeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Екатеринбургский метрополитен", url="https://metro-ektb.ru/")
        ],
        [
            InlineKeyboardButton(text="ЕКАРТА", url="http://www.ekarta-ek.ru/")
        ],
        [
            InlineKeyboardButton(text="ЕМУП «ГОРТРАНС»", url="https://ekatgortrans.ru/")
        ],
    ]
)
