from aiogram import types

from database.models import User
from keyboards.subscribe import subscribe_keyboard
from loader import dp
from utils.check_membership import check_membership


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user: types.User = message.from_user
    if await User.get_user(user.id) is None:
        await User.create_user()
    if not await check_membership(user.id):
        await message.answer('...', reply_markup=subscribe_keyboard())
        return
    await message.answer_chat_action('typing')
    await message.answer('OK...')
