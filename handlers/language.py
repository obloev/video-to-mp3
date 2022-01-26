from aiogram import types
from aiogram.utils.callback_data import CallbackData

from database.db import db
from keyboards.subscribe import subscribe_keyboard
from loader import dp
from utils.check_membership import check_membership

language_cd = CallbackData('language', 'lang')


@dp.callback_query_handlers(language_cd.filter(lang='*'))
def set_language(query: types.CallbackQuery, callback_data: dict):
    await query.answer()
    lang = callback_data['lang']
    await db.set_language(lang)
    await query.message.delete()
    is_member = await check_membership(query.from_user.id)
    if not is_member:
        await query.message.answer('please subscribe', reply_markup=subscribe_keyboard())
        return
    await query.message.answer('OKK')
