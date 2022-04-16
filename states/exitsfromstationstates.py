from aiogram.dispatcher.filters.state import StatesGroup, State


class ExitsFromStation(StatesGroup):
    TakeStation = State()
