from discord import Message
from discord.ext import commands
from marsbots.platforms.discord.util import is_mentioned


def on_mention(bot: commands.Bot, message: Message) -> bool:
    return is_mentioned(message, bot.user)
