from aiogram import executor, types
from bot_handlers import register_handlers_common
from bot_config import dp


if __name__ == "__main__":
    register_handlers_common(dp)
    executor.start_polling(dp, skip_updates=True)
