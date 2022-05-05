import requests
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot_package import create_toilet_in_DB, find_loc_to_answer, get_addres_by_location
from bot_states import ToiletState, NearToiletState


async def start_handler(message):
    await message.answer(
        "Привет, друг!\nТы наверное очень хочешь запостить новый туалет?\nЖми /post и заполняй анкету!")


async def get_location(message: types.Message):
    await message.answer("Отправьте локацию")
    await ToiletState.location.set()


async def get_description(message: types.Message, state: FSMContext):
    await state.update_data(location=f"{message.location.latitude}, {message.location.longitude}")
    await message.answer("Отлично!\nТеперь введите описание")
    await ToiletState.description.set()


async def get_rating(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Отлично! Теперь оцените туалет от 1 до 10")
    await ToiletState.rating.set()


async def send_req(message: types.Message, state: FSMContext):
    if 1 <= int(message.text) <= 10:
        await state.update_data(rating=int(message.text))
        await state.update_data(user_name=message.from_user.username)
        await state.update_data(user_tg_id=message.from_user.id)
        data = await state.get_data()
        await state.finish()
        await message.answer("Готово!")

        create_toilet_in_DB(data)


async def toilet_list(message):
    get_response = requests.get("http://127.0.0.1:8000/api/toilets/list/")
    for toilet in get_response.json():
        await message.answer(
            f"{toilet['author']}\n{toilet['address']}\n{toilet['description']}\n{toilet['rating']}\n{toilet['user_tg_id']}\n{toilet['location']}\n------------------------")


async def toilet_list_personolized(message):
    get_response = requests.get(f"http://127.0.0.1:8000/api/toilets/list/{message.from_user.id}/")
    for toilet in get_response.json():
        await message.answer(
            f"{toilet['author']}\n{toilet['address']}\n{toilet['description']}\n{toilet['rating']}\n{toilet['user_tg_id']}\n{toilet['location']}\n------------------------")


async def near_toilet(message):
    await message.answer('Пришлите геоданные, чтобы мы нашли вам туалет поблизости')
    await NearToiletState.location.set()


async def near_toilet_getloc(message: types.Message, state: FSMContext):
    await state.update_data(location={'lat': message.location['latitude'], 'lon': message.location['longitude']})
    data = await state.get_data()
    await state.finish()
    loc_to_get_address = f"{data['location']['lat']}, {data['location']['lon']}"
    loc_to_answer = find_loc_to_answer(data)
    await message.reply_location(loc_to_answer['lat'], loc_to_answer['lon'])
    await message.answer(get_addres_by_location(loc_to_get_address))


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(get_location, commands=["post"])
    dp.register_message_handler(get_description, state=ToiletState.location, content_types=['location'])
    dp.register_message_handler(get_rating, state=ToiletState.description, content_types=['text'])
    dp.register_message_handler(send_req, state=ToiletState.rating, content_types=['text'])
    # -------------------
    dp.register_message_handler(toilet_list, commands=["get"])
    dp.register_message_handler(toilet_list_personolized, commands=["getmy"])
    dp.register_message_handler(near_toilet, commands=["near"])
    dp.register_message_handler(near_toilet_getloc, state=NearToiletState.location, content_types=['location'])
