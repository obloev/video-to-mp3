from aiogram import types

from database.models import User
from loader import dp


@dp.message_handler(commands=['count'])
async def count(message: types.Message):
    users_count = await User.users_count()
    await message.answer_chat_action('typing')
    await message.answer(f'Number of users {users_count}')
