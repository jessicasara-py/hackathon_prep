import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

_client = None  # wird nur einmal erzeugt und dann wiederverwendet


def get_model() -> str:
    return os.getenv("OPENAI_MODEL", "gpt-5-nano")


def get_ai_client() -> OpenAI:
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise SystemExit("Error: OPENAI_API_KEY is missing in the .env")
        _client = OpenAI(api_key=api_key)
    return _client