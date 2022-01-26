from aiogram import types
from aiogram.utils.callback_data import CallbackData

from loader import dp
from utils.check_membership import check_membership

subscribe_cd = CallbackData('subscribe', 'action')


@dp.callback_query_handlers(subscribe_cd.filter(action='confirm'))
def check_membership_data(query: types.CallbackQuery) -> None:
    await query.answer()
    is_member = await check_membership(query.from_user.id)
    if not is_member:
        query.answer('No member', show_alert=True)
        return
    await query.message.delete()
    await query.answer('OKK')
