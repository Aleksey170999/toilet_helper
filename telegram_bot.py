import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot_package import create_toilet_in_DB
import requests


logging.basicConfig(level=logging.INFO)

API_TOKEN = "5138294873:AAE68AoN0KARSwcXUWUx8i0wtyJBifRxTtU"

storage = MemoryStorage()

dp = Dispatcher(bot=Bot(API_TOKEN), storage=storage)


class ToiletState(StatesGroup):
    location = State()
    description = State()
    rating = State()


@dp.message_handler(commands=["start"])
async def start_handler(message):
    await message.answer(
        "Привет, друг!\nТы наверное очень хочешь запостить новый туалет?\nЖми /post и заполняй анкету!")


@dp.message_handler(commands=['post'])
async def user_register(message: types.Message):
    await message.answer("Отправьте локацию")
    await ToiletState.location.set()


@dp.message_handler(state=ToiletState.location, content_types=['location'])
async def get_location(message: types.Message, state: FSMContext):
    await state.update_data(location=f"{message.location.latitude}, {message.location.longitude}")
    await message.answer("Отлично! Теперь введите описание: ")
    await ToiletState.next()


@dp.message_handler(state=ToiletState.description, content_types=['text'])
async def get_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Отлично! Теперь введите rating: ")
    await ToiletState.next()


@dp.message_handler(state=ToiletState.rating, content_types=['text'])
async def get_rating(message: types.Message, state: FSMContext):
    if 0 <= int(message.text) <= 5:
        await state.update_data(rating=int(message.text))
        await state.update_data(user_name=message.from_user.username)
        await state.update_data(user_tg_id=message.from_user.id)
        await message.answer("Ура!")
        data = await state.get_data()
        await state.finish()

        create_toilet_in_DB(data)


@dp.message_handler(commands=['get'])
async def toilet_list(message):
    get_response = requests.get("http://127.0.0.1:8000/api/toilets/list/")
    for toilet in get_response.json():
        await message.answer(f"{toilet['author']}\n{toilet['address']}\n{toilet['description']}\n{toilet['rating']}\n{toilet['user_tg_id']}\n{toilet['location']}\n------------------------")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
