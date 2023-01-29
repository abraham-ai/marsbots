from functools import partial
from typing import Any, Callable
from marsbots.platforms.discord.capabilities import ChatCapability
from marsbots.platforms.discord.modifiers import (
    in_channels,
    in_guilds,
    not_in_channels,
    not_in_guilds,
)

from marsbots.platforms.discord.triggers import on_mention


def transform_trigger(trigger: str) -> Callable:
    if trigger == "onMention":
        return on_mention
    raise ValueError(f"Trigger {trigger} not found.")


def transform_modifier(modifier: dict) -> Callable:
    if modifier["type"] == "inChannels":
        channels = [int(channel) for channel in modifier["data"]["channels"]]
        return partial(in_channels, channels)
    elif modifier["type"] == "inGuilds":
        guilds = [int(guild) for guild in modifier["data"]["channels"]]
        return partial(in_guilds, guilds)
    elif modifier["type"] == "notInChannels":
        channels = [int(channel) for channel in modifier["data"]["channels"]]
        return partial(not_in_channels, channels)
    elif modifier["type"] == "notInGuilds":
        guilds = [int(guild) for guild in modifier["data"]["channels"]]
        return partial(not_in_guilds, guilds)
    raise ValueError(f"modifier {modifier} not found.")


def transform_capability(capability: dict) -> Any:
    if capability["type"] == "chat":
        prompt = capability["data"]["prompt"]
        return ChatCapability(prompt)
    raise ValueError(f"Capability {capability} not found.")
