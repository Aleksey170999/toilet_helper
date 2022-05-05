from aiogram.dispatcher.filters.state import State, StatesGroup


class ToiletState(StatesGroup):
    location = State()
    description = State()
    rating = State()


class NearToiletState(StatesGroup):
    location = State()