from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.exceptions import BotBlocked, UserDeactivated

from database.models import User
from loader import dp
from utils.config import ADMIN


class Post(StatesGroup):
    get_post: State = State()


@dp.message_handler(state=Post.get_post)
async def send_post(message: types.Message, state: FSMContext):
    users = await User.get_users()
    sent = 0
    failed = 0
    await message.answer_chat_action('typing')
    mes = await message.reply('<b>📝 Preparing to post ...</b>')
    for user in users:
        try:
            await message.copy_to(user.user_id)
            sent += 1
        except (BotBlocked, UserDeactivated):
            await User.delete_user(user.user_id)
            failed += 1
        if (sent + failed) % 3 == 0:
            await mes.edit_text(f'<b>📝 Posting ...\n\n✅ Sent - {sent}\n🚫 Failed: {failed}</b>')
    await mes.edit_text(f'<b>✔️ Complete\n\n✅ Sent - {sent}\n🚫 Failed: {failed}</b>')
    await state.finish()


@dp.message_handler(lambda mes: mes.from_user.id == ADMIN, commands=['post'])
async def post(message: types.Message):
    await message.answer_chat_action('typing')
    await message.reply('<b>📝 Send the post</b>')
    await Post.get_post.set()
