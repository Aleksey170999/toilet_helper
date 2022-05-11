from aiogram import executor
from bot_handlers import register_handlers_common
from bot_config import dp


if __name__ == "__main__":
    register_handlers_common(dp)
    executor.start_polling(dp, skip_updates=True)


# import time
# import pyautogui
#
# time.sleep(3)
#
# x = 0
# while x < 1000:
#     pyautogui.press('1')
#     pyautogui.press('esc')
#     x += 1
#     time.sleep(0.5)
