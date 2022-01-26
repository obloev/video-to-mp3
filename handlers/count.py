from aiogram import types

from database.db import db
from loader import dp


@dp.message_handler(commands=['count'])
async def count(message: types.Message):
    users_count = await db.users_count()
    await message.answer(f'Number of users {users_count}')
