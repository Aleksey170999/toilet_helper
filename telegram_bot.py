import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import bot_handlers

logging.basicConfig(level=logging.INFO)

API_TOKEN = "5138294873:AAE68AoN0KARSwcXUWUx8i0wtyJBifRxTtU"

storage = MemoryStorage()

dp = Dispatcher(bot=Bot(API_TOKEN), storage=storage)


class ToiletState(StatesGroup):
    location = State()
    description = State()
    rating = State()


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(bot_handlers.start_handler, commands=["start"])
    dp.register_message_handler(bot_handlers.get_location, commands=["post"])
    dp.register_message_handler(bot_handlers.get_description, state=ToiletState.location, content_types=['location'])
    dp.register_message_handler(bot_handlers.get_rating, state=ToiletState.description, content_types=['text'])
    dp.register_message_handler(bot_handlers.send_req, state=ToiletState.rating, content_types=['text'])
    dp.register_message_handler(bot_handlers.toilet_list, commands=["get"])
    dp.register_message_handler(bot_handlers.toilet_list_personolized, commands=["getmy"])


if __name__ == "__main__":
    register_handlers_common(dp)
    executor.start_polling(dp, skip_updates=True)
