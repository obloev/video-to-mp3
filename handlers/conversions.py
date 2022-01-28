from aiogram.types import Message

from database.models import User
from loader import dp
from utils.config import ADMIN


@dp.message_handler(lambda mes: mes.from_user.id == ADMIN, commands=['conversions'])
async def conversions_handler(message: Message):
    await message.answer_chat_action('typing')
    mes: Message = await message.reply('**🎵 Counting ...**')
    users = await User.get_users(admin=True)
    conversions: int = 0
    for user in users:
        conversions += user.conversions
    await mes.edit_text(f'**🎵 Total number of conversions - {conversions}**')
