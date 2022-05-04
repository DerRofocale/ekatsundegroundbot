from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


adminmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить админа"),
            KeyboardButton(text="Удалить админа"),
        ],
        [
            KeyboardButton(text="Список админов"),
            KeyboardButton(text="Список пользователей"),
        ],
        [
            KeyboardButton(text="Статистика использования")
        ],
        [
            KeyboardButton(text="Рассылка"),
            KeyboardButton(text="Выйти из админ-панели"),
        ],
    ],
    resize_keyboard=True
)

adminYesOrNo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True

)


spamChoise = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Текст"),
            KeyboardButton(text="Текст + фото"),
            KeyboardButton(text="Фото"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True

)


returnAdminPanel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отменить действие"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
