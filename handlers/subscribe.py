from aiogram import types
from aiogram.utils.callback_data import CallbackData

from loader import dp
from utils.check_membership import check_membership

subscribe_cd = CallbackData('subscribe', 'action')


@dp.callback_query_handler(subscribe_cd.filter(action='confirm'))
async def check_membership_data(query: types.CallbackQuery) -> None:
    is_member = await check_membership(query.from_user.id)
    if not is_member:
        await query.message.answer_chat_action('typing')
        await query.answer('No member', show_alert=True)
        return
    await query.message.delete()
    await query.message.answer_chat_action('typing')
    await query.message.answer('welcome')
