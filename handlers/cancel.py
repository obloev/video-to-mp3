from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(commands=['cancel'], state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply('<b>❌ Canceled</b>')
