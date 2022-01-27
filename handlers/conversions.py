from aiogram import types

from database.models import User
from loader import dp
from utils.config import ADMIN


@dp.message_handler(lambda mes: mes.from_user.id == ADMIN, commands=['conversions'])
async def conversions_handler(message: types.Message):
    mes = await message.answer('Counting ...')
    users = await User.get_users()
    conversions = 0
    for user in users:
        conversions += user.conversions
    await mes.edit_text(str(conversions))

