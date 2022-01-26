from aiogram import types

from handlers.video import filename_cd


def filename_keyboard(filename) -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton('Yes', callback_data=filename_cd.new(bool=True, name=filename)),
        types.InlineKeyboardButton('No', callback_data=filename_cd.new(bool=False, name=filename)),
    )
