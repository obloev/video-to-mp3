from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.post import Post
from loader import dp


@dp.message_handler(commands=['cancel'], state=Post.get_post)
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply('<b>❌ Canceled</b>')
