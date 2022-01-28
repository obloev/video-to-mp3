from aiogram import types, Dispatcher

from utils.config import ADMIN


async def set_default_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🤖 Launch the bot"),
            types.BotCommand("count", "👤 Number of users"),
            types.BotCommand("conversions", "🎵 All conversions count"),
            types.BotCommand("post", "📝 Send a post"),
            types.BotCommand("cancel", "🚫 Cancel posting"),
            types.BotCommand("developer", "🧑‍💻 Developer of the bot"),
        ], scope=types.BotCommandScopeChat(ADMIN)
    )
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🤖 Launch the bot"),
            types.BotCommand("count", "👤 Number of users"),
            types.BotCommand("developer", "‍💻 Developer of the bot"),
        ]
    )
