from aiogram import executor

from database.db import connect_db
from handlers import set_handlers
from loader import dp
from utils.notify_admin import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await connect_db()
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    set_handlers()


async def on_shutdown(dispatcher):
    await on_shutdown_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
