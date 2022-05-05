from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging


logging.basicConfig(level=logging.INFO)

API_TOKEN = "5138294873:AAE68AoN0KARSwcXUWUx8i0wtyJBifRxTtU"

storage = MemoryStorage()

dp = Dispatcher(bot=Bot(API_TOKEN), storage=storage)