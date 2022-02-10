from aiogram.dispatcher.filters.state import StatesGroup, State


class Converter(StatesGroup):
    from_cur = State()
    to_cur = State()
    amount = State()