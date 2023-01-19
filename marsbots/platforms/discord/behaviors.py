from bson import ObjectId
from discord import Message
from manifest import Manifest
from marsbots.platforms.discord.models import Marsbot
from marsbots.platforms.discord.util import (
    remove_role_mentions,
    replace_bot_mention,
    replace_mentions_with_usernames,
)

from marsbots.util import generate_run_id


class CharacterBehavior:
    def __init__(self, bot: Marsbot, llm: Manifest) -> None:
        self.llm = llm
        self.bot = bot
        # self.prompt = self.load_prompt()
        self.prompt = "hey"

    def load_prompt(self) -> str:
        db = self.bot.db
        personality = db.personalities.find_one({"_id": ObjectId(self.bot.metadata.id)})
        return personality["prompt"]

    async def reply_to_message(self, message: Message):
        ctx = await self.bot.get_context(message)
        async with ctx.channel.typing():
            prompt = self.prompt.replace(
                "{{recentMessage}}", self.message_preprocessor(message)
            )
            completion = self.llm.run(prompt=prompt, run_id=generate_run_id())
            await message.reply(completion)

    def message_preprocessor(self, message: Message) -> str:
        message_content = replace_bot_mention(message.content, only_first=True)
        message_content = replace_mentions_with_usernames(
            message_content,
            message.mentions,
        )
        message_content = remove_role_mentions(message_content)
        message_content = message_content.strip()
        return message_content
