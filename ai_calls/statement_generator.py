import json
import random
from openai.types.chat import ChatCompletionMessageParam
from ai_calls.ai_client import get_ai_client, get_model

MAX_TEXT_CHARS = 4000   # so viel Artikeltext bekommt die KI (spart Tokens/Kosten)

SYSTEM_PROMPT = """You will create statements for a true/false quiz based on Wikipedia articles.
Rules:
- Exactly ONE statement, one sentence, in English, understandable to non-experts.
- Use ONLY facts from the given article text.
- A TRUE statement must be clearly supported by the text.
- A FALSE statement must sound plausible but must misrepresent exactly one specific detail
  (e.g., year, number, place, person) and be clearly false according to the text.
- Do not use phrases such as “according to the article” or “in the text.”
- respond in english 
Respond exclusively in JSON format:
{"statement": "...", "explanation": "brief justification with the correct fact"}"""


def generate_statement(title: str, text: str) -> dict:
    """
    Erzeugt eine Quiz-Aussage zu einem Artikel.
    Rückgabe: {"aussage": str, "erfunden": bool, "erklaerung": str}
    """
    # Wir würfeln selbst, ob die Aussage wahr oder erfunden sein soll.
    # So ist die Verteilung fair 50:50 und hängt nicht von der KI ab.
    erfunden = random.choice([True, False])
    art = "FALSE (invented)" if erfunden else "TRUE"

    user_prompt = (
        f"Create a {art} Statement.\n\n"
        f"Article: {title}\n\n"
        f"Text:\n{text[:MAX_TEXT_CHARS]}"
    )

    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    response = get_ai_client().chat.completions.create(
        model=get_model(),
        messages=messages,
        response_format={"type": "json_object"},   # erzwingt gültiges JSON
    )

    content = response.choices[0].message.content
    if not content:
        raise ValueError("AI did not provide a response")

    data = json.loads(content)

    if not data.get("statement"):
        raise ValueError(f"AI response without a statement: {data}")

    return {
        "aussage": data["statement"],
        "erfunden": erfunden,
        "erklaerung": data.get("explanation", ""),
    }

SYSTEM_PROMPT = """You will create statements for a true/false quiz based on Wikipedia articles.
Rules:
- Exactly ONE statement, one sentence, in English, understandable to non-experts.
- Use ONLY facts from the given article text.
- A TRUE statement must be clearly supported by the text.
- A FALSE statement must sound plausible but must misrepresent exactly one specific detail
  (e.g., year, number, place, person) and be clearly false according to the text.
- Do not use phrases such as “according to the article” or “in the text.”
- respond in english 
Respond exclusively in JSON format:
{"statement": "...", "explanation": "brief justification with the correct fact"}"""


def generate_statement(title: str, text: str) -> dict:
    """
    Erzeugt eine Quiz-Aussage zu einem Artikel.
    Rückgabe: {"aussage": str, "erfunden": bool, "erklaerung": str}
    """
    # Wir würfeln selbst, ob die Aussage wahr oder erfunden sein soll.
    # So ist die Verteilung fair 50:50 und hängt nicht von der KI ab.
    erfunden = random.choice([True, False])
    art = "FALSE (invented)" if erfunden else "TRUE"

    user_prompt = (
        f"Create a {art} Statement.\n\n"
        f"Article: {title}\n\n"
        f"Text:\n{text[:MAX_TEXT_CHARS]}"
    )

    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    response = get_ai_client().chat.completions.create(
        model=get_model(),
        messages=messages,
        response_format={"type": "json_object"},   # erzwingt gültiges JSON
    )

    content = response.choices[0].message.content
    if not content:
        raise ValueError("AI did not provide a response")

    data = json.loads(content)

    if not data.get("statement"):
        raise ValueError(f"AI response without a statement: {data}")

    return {
        "aussage": data["statement"],
        "erfunden": erfunden,
        "erklaerung": data.get("explanation", ""),
    }

