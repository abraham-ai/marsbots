import os
from manifest import Manifest
from manifest.caches.redis import RedisCache
from marsbots.util import generate_run_id


class CharacterCapability:
    def __init__(self, name: str, prompt: str, api_key: str, use_cache: bool = False):
        self.name = name
        self.prompt = prompt
        self.llm = Manifest(
            client_name="openai",
            client_connection=api_key,
            max_tokens=100,
            temperature=1.0,
            stop_token="<",
        )
        redis_uri = os.getenv("REDIS_URI")
        if use_cache and redis_uri:
            self.llm.cache = RedisCache(
                connection_str=redis_uri,
            )

    def reply_to_message(self, message: str, sender_name: str):
        prompt = self.prompt
        prompt = prompt.replace("{{recentMessage}}", message)
        completion = self.llm.run(prompt=prompt, run_id=generate_run_id())
        return completion
