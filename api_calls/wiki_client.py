import os
import wikipediaapi
from dotenv import load_dotenv

load_dotenv()

_wiki = None  # wird nur einmal erzeugt und dann wiederverwendet


def get_language() -> str:
    return os.getenv("WIKI_LANGUAGE", "de")


def get_user_agent() -> str:
    """User-Agent für alle Wikimedia-Anfragen (auch für direkte requests-Aufrufe)."""
    app_name = os.getenv("WIKI_APP_NAME", "WikiTrivia")
    contact = os.getenv("WIKI_CONTACT")
    if not contact:
        raise SystemExit("Fehler: WIKI_CONTACT fehlt in der .env")
    return f"{app_name} ({contact})"


def get_wiki() -> wikipediaapi.Wikipedia:
    """
    def get_wiki() definiert eine Funktion ohne Parameter.
    -> wikipediaapi.Wikipedia bedeutet, dass sie ein Objekt der Klasse Wikipedia
       aus dem Modul wikipediaapi zurückgibt.

    Die Hints sind also optional und dienen vor allem dazu, dass
    PyCharm Autovervollständigung anbietet (nach get_wiki(). kennt es z. B. .page()),
    """

    global _wiki
    if _wiki is None:
        _wiki = wikipediaapi.Wikipedia(
            user_agent=get_user_agent(),
            language=get_language(),
        )
    return _wiki
