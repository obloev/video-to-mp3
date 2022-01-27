from aiogram import types, Dispatcher

from utils.config import ADMIN


async def set_default_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Run the bot"),
            types.BotCommand("developer", "Developer of the bot"),
            types.BotCommand("count", "Number of users"),
            types.BotCommand("post", "Sen a post"),
            types.BotCommand("conversions", "All conversions count"),
        ], scope=types.BotCommandScopeChat(ADMIN)
    )
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Run the bot"),
            types.BotCommand("developer", "Developer of the bot"),
            types.BotCommand("count", "Number of users")
        ]
    )
