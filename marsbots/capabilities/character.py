from manifest import Manifest
from marsbots.util import generate_run_id


class CharacterCapability:
    def __init__(self, name: str, prompt: str, api_key: str, cache_connection: str):
        self.name = name
        self.prompt = prompt
        self.llm = Manifest(
            client_name="openai",
            client_connection=api_key,
            max_tokens=100,
            temperature=1.0,
            stop_token="<",
            cache_name="redis",
            cache_connection=cache_connection,
        )

    def reply_to_message(self, message: str, sender_name: str):
        prompt = self.prompt
        prompt += "\n\n"
        prompt += f'<{sender_name}> "{message}"\n'
        prompt += f"<{self.name}>"
        completion = self.llm.run(prompt=prompt, run_id=generate_run_id())
        return completion
