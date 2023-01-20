from abc import ABC, abstractmethod

from discord import Message
from marsbots.platforms.discord.util import (
    remove_role_mentions,
    replace_bot_mention,
    replace_mentions_with_usernames,
)

from marsbots.util import generate_run_id


class Behavior(ABC):
    @abstractmethod
    async def call(self, bot, message: Message):
        pass


class CharacterBehavior(Behavior):
    def __init__(self, prompt: str):
        self.prompt = prompt

    async def call(self, bot, message: Message):
        def message_preprocessor(message: Message) -> str:
            message_content = replace_bot_mention(message.content, only_first=True)
            message_content = replace_mentions_with_usernames(
                message_content,
                message.mentions,
            )
            message_content = remove_role_mentions(message_content)
            message_content = message_content.strip()
            return message_content

        ctx = await bot.get_context(message)
        async with ctx.channel.typing():
            prompt = self.prompt.replace(
                "{{recentMessage}}", message_preprocessor(message)
            )
            completion = bot.llm.run(prompt=prompt, run_id=generate_run_id())
            await message.reply(completion)
