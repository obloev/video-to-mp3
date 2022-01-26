from aiogram import types

from database.db import db
from database.models import User
from keyboards.language import lang_keyboard
from loader import dp


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    if await User.get_user(user.id) is None:
        await User.create_user()
        print('created')
    if not await db.get_lang(user.id):
        await message.answer('choose lang', reply_markup=lang_keyboard())
        return
