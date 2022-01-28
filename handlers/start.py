from aiogram import types

from database.models import User
from keyboards.subscribe import subscribe_keyboard
from loader import dp, bot
from utils.check_membership import check_membership
from utils.config import CHANNEL, JOINCHAT_URL, GROUP


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user: types.User = message.from_user
    await bot.send_message(GROUP, f'[{user.full_name}](tg://user?id={user.id}) launched  **THE BOT**')
    if await User.get_user(user.id) is None:
        await User.create_user()
    if not await check_membership(user.id):
        await message.answer(f'**Subscribe to the channel to use the bot [{CHANNEL}]({JOINCHAT_URL})**',
                             reply_markup=subscribe_keyboard())
        return
    await message.answer_chat_action('typing')
    await message.answer(f'**👋 Hi [{user.full_name}](tg://user?id={user.id}).'
                         f'This bot converts video files to 🎵 MP3 format**')
