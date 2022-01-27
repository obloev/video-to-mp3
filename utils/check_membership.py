from aiogram.types import ChatMember, ChatMemberBanned, ChatMemberLeft

from loader import bot
from utils.config import CHANNEL


async def check_membership(user_id):
    membership: ChatMember = await bot.get_chat_member(CHANNEL, user_id)
    if membership.status not in ['left', 'banned']:
        return True
    return False
