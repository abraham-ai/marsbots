import os
from functools import partial

import discord
from discord.ext import commands
from marsbots.models import Capability
from marsbots.platforms.discord.behaviors import CharacterBehavior
from marsbots.platforms.discord.checks import in_channels
from marsbots.platforms.discord.externals import init_llm
from marsbots.platforms.discord.models import MarsbotMetadata
from marsbots.platforms.discord.triggers import on_mention
from pymongo import MongoClient


UNLIKELY_PREFIX = ["438974983724798uyfsduhfksdhfjhksdbfhjgsdyfgsdygfusd"]


class MarsBot(commands.Bot):
    def __init__(self, metadata: MarsbotMetadata) -> None:
        self.metadata = metadata

        client = MongoClient(os.getenv("MONGODB_URI"))
        self.db = client["marsbots"]

        intents = discord.Intents.default()
        self.set_intents(intents)

        self.llm = init_llm()

        self.capabilities = [
            Capability(
                trigger=on_mention,
                checks=[partial(in_channels, [876235075145064488])],
                behavior=CharacterBehavior(self, self.llm).reply_to_message,
            )
        ]
        super().__init__(
            command_prefix=UNLIKELY_PREFIX,
            intents=intents,
        )

    def set_intents(self, intents: discord.Intents) -> None:
        intents.message_content = True
        intents.messages = True
        if self.metadata.intents:
            if "presence" in self.metadata.intents:
                intents.presences = True
            if "members" in self.metadata.intents:
                intents.members = True

    async def on_ready(self) -> None:
        print(f"Running {self.metadata.name}...")

    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return
        for capability in self.capabilities:
            if capability.trigger(self, message):
                for check in capability.checks:
                    if not check(message):
                        await message.reply("This command is not available here.")
                        return
                await capability.behavior(message)

        await self.process_commands(message)
