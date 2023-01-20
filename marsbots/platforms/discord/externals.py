import os
from manifest import Manifest
from manifest.caches.redis import RedisCache


def init_llm():
    llm = Manifest(
        client_name="openai",
        client_connection=os.getenv("OPENAI_API_KEY"),
        max_tokens=100,
        temperature=1.0,
        stop_token="<",
    )
    redis_uri = os.getenv("REDIS_URI")
    if redis_uri:
        llm.cache = RedisCache(
            connection_str=redis_uri,
        )
    return llm
