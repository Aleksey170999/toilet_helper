import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot_package import create_toilet_in_DB
from telegram_bot import ToiletState


async def start_handler(message):
    await message.answer(
        "Привет, друг!\nТы наверное очень хочешь запостить новый туалет?\nЖми /post и заполняй анкету!")


async def get_location(message: types.Message):
    await message.answer("Отправьте локацию")
    await ToiletState.location.set()


async def get_description(message: types.Message, state: FSMContext):
    await state.update_data(location=f"{message.location.latitude}, {message.location.longitude}")
    await message.answer("Отлично!\nТеперь введите описание")
    await ToiletState.next()


async def get_rating(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Отлично! Теперь оцените туалет от 0 до 5")
    await ToiletState.next()


async def send_req(message: types.Message, state: FSMContext):
    if 0 <= int(message.text) <= 5:
        await state.update_data(rating=int(message.text))
        await state.update_data(user_name=message.from_user.username)
        await state.update_data(user_tg_id=message.from_user.id)
        await message.answer("Ура!\nОжидайте, пока пост пройдет модерацию...")
        data = await state.get_data()
        await state.finish()
        create_toilet_in_DB(data)


async def toilet_list(message):
    get_response = requests.get("http://127.0.0.1:8000/api/toilets/list/")
    for toilet in get_response.json():
        await message.answer(f"{toilet['author']}\n{toilet['address']}\n{toilet['description']}\n{toilet['rating']}\n{toilet['user_tg_id']}\n{toilet['location']}\n------------------------")


async def toilet_list_personolized(message):
    get_response = requests.get(f"http://127.0.0.1:8000/api/toilets/list/{message.from_user.id}/")
    for toilet in get_response.json():
        await message.answer(f"{toilet['author']}\n{toilet['address']}\n{toilet['description']}\n{toilet['rating']}\n{toilet['user_tg_id']}\n{toilet['location']}\n------------------------")

