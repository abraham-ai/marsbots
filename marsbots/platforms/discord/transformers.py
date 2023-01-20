from functools import partial
from typing import Callable
from discord import Any
from marsbots.platforms.discord.behaviors import CharacterBehavior
from marsbots.platforms.discord.checks import (
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


def transform_check(check: dict) -> Callable:
    if check["type"] == "inChannels":
        channels = [int(channel) for channel in check["data"]["channels"]]
        return partial(in_channels, channels)
    elif check["type"] == "inGuilds":
        guilds = [int(guild) for guild in check["data"]["channels"]]
        return partial(in_guilds, guilds)
    elif check["type"] == "notInChannels":
        channels = [int(channel) for channel in check["data"]["channels"]]
        return partial(not_in_channels, channels)
    elif check["type"] == "notInGuilds":
        guilds = [int(guild) for guild in check["data"]["channels"]]
        return partial(not_in_guilds, guilds)
    raise ValueError(f"Check {check} not found.")


def transform_behavior(behavior: dict) -> Any:
    print("ccc", type(behavior))
    if behavior["type"] == "character":
        prompt = behavior["data"]["prompt"]
        return CharacterBehavior(prompt)
    raise ValueError(f"Behavior {behavior} not found.")
