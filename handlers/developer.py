from aiogram import types

from loader import dp


@dp.message_handler(commands=['developer'])
async def start(message: types.Message):
    await message.answer('Obloev Komronbek @TGBotsAdminBot')
