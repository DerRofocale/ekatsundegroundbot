from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


startkeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ближайший поезд"),

        ],
        [
            KeyboardButton(text="Схема выходов"),

        ]
    ],
    resize_keyboard=True
)

stationskeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Проспект Космонавтов"),
        ],
        [
            KeyboardButton(text="Уралмаш"),
            KeyboardButton(text="Машиностроителей")
        ],
        [
            KeyboardButton(text="Уральская"),
            KeyboardButton(text="Динамо")
        ],
        [
            KeyboardButton(text="Площадь 1905 года"),
        ],
        [
            KeyboardButton(text="Геологическая"),
            KeyboardButton(text="Чкаловская"),
        ],
        [
            KeyboardButton(text="Ботаническая"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

towherekeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Проспект Космонавтов"),
        ],
        [
            KeyboardButton(text="Ботаническая"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)