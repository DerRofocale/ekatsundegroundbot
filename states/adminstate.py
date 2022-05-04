from aiogram.dispatcher.filters.state import StatesGroup, State


class ADMPNL(StatesGroup):
    ADMIN = State()
    AddNewAdmin1 = State()
    AddNewAdmin2 = State()
    AddNewHostes1 = State()
    AddNewHostes2 = State()
    DeleteAdmin1 = State()
    DeleteAdmin2 = State()
    DeleteAdminYesOrNo = State()
    SPAM = State()
    SPAMText = State()
    SPAMPhoto = State()
    SPAMTextAndPhoto = State()
    SPAMTextAndPhoto1 = State()
    SPAMTextAndPhoto2 = State()
    SPAMTextAndPhoto3 = State()
    SPAMYesOrNoText = State()
    SPAMYesOrNoTextAndPhoto = State()
    SPAMYesOrNoPhoto = State()
