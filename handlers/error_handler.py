import logging
from aiogram.utils.exceptions import TelegramAPIError, MessageNotModified, CantParseEntities

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    if isinstance(exception, MessageNotModified):
        logging.exception(MessageNotModified.match.capitalize())
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'{CantParseEntities.match.capitalize()}: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'Telegram API Error: {exception} \nUpdate: {update}')
        return True

    logging.exception(f'Update: {update} \n{exception}')
