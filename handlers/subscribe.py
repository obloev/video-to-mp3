from aiogram import types
from aiogram.utils.callback_data import CallbackData

from loader import dp, bot
from utils.check_membership import check_membership
from utils.config import GROUP

subscribe_cd: CallbackData = CallbackData('subscribe', 'action')


@dp.callback_query_handler(subscribe_cd.filter(action='confirm'))
async def check_membership_data(query: types.CallbackQuery) -> None:
    is_member = await check_membership(query.from_user.id)
    if not is_member:
        await query.message.answer_chat_action('typing')
        await query.answer("🚫 You aren't a member of the channel", show_alert=True)
        return
    await query.message.delete()
    await query.message.answer_chat_action('typing')
    user = query.from_user
    await bot.send_message(GROUP, f'<a href="tg://user?id={user.id}">{user.full_name}</a> joined <b>THE CHANNEL</b>')
    await query.message.answer(f'<b>👋 Hi <a href="tg://user?id={user.id}">{user.full_name}</a>.'
                               f'This bot converts video files to 🎵 MP3 format</b>')
