from aiogram import types

from handlers.subscribe import subscribe_cd
from utils.config import JOINCHAT_URL


def subscribe_keyboard() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton('🔗', url=JOINCHAT_URL),
        types.InlineKeyboardButton('✔️', callback_data=subscribe_cd.new(action='confirm')),
    )
