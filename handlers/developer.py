from aiogram import types

from loader import dp
from utils.config import ADMIN_BOT


@dp.message_handler(commands=['developer'])
async def start(message: types.Message):
    await message.answer_chat_action('typing')
    await message.answer(f'**🧑‍💻 Developer:** Obloev Komronbek {ADMIN_BOT}')
