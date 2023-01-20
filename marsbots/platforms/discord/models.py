from dataclasses import dataclass
from typing import Optional

from discord.ext import commands

from pymongo import MongoClient


@dataclass
class MarsbotMetadata:
    name: str

    intents: Optional[list[str]] = None
    command_prefix: Optional[str] = None


@dataclass
class Marsbot(commands.Bot):
    metadata: MarsbotMetadata
    db: MongoClient
