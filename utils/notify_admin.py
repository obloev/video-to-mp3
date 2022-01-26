import logging
from aiogram import Dispatcher

from utils.config import ADMIN


async def on_startup_notify(dp: Dispatcher) -> None:
    try:
        await dp.bot.send_message(ADMIN, "Bot launched")
    except Exception as err:
        logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMIN, "Bot stopped")
    except Exception as err:
        logging.exception(err)
