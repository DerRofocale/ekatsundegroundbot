from aiogram.dispatcher.filters.state import StatesGroup, State


class SoonTrain(StatesGroup):
    TakeStation = State()
    TakeToWhere = State()
