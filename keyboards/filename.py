from aiogram import types
from aiogram.utils.callback_data import CallbackData

filename_cd = CallbackData('filename', 'action')


def filename_keyboard() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton('✅ Yes', callback_data=filename_cd.new(action='yes')),
        types.InlineKeyboardButton('🚫 No', callback_data=filename_cd.new(action='no')),
    )
