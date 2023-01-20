from discord import Message


def in_channels(channel_ids: list[int], message: Message):
    return message.channel.id in channel_ids


def in_guilds(guild_ids: list[int], message: Message):
    if not message.guild:
        return False
    return message.guild.id in guild_ids


def not_in_channels(channel_ids: list[int], message: Message):
    return message.channel.id not in channel_ids


def not_in_guilds(guild_ids: list[int], message: Message):
    if not message.guild:
        return False

    return message.guild.id not in guild_ids
