from aiogram import types

from handlers.language import language_cd


def lang_keyboard() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton('uz', callback_data=language_cd.new(lang='uz')),
        types.InlineKeyboardButton('ru', callback_data=language_cd.new(lang='ru')),
        types.InlineKeyboardButton('en', callback_data=language_cd.new(lang='en'))
    )
