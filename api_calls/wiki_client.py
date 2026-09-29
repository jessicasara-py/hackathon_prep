import os
import wikipediaapi
from dotenv import load_dotenv

load_dotenv()

_wiki = None

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
        app_name = os.getenv("WIKI_APP_NAME", "WikiTrivia")
        contact = os.getenv("WIKI_CONTACT")
        language = os.getenv("WIKI_LANGUAGE", "de")

        if not contact:
            raise SystemExit("Fehler: WIKI_CONTACT fehlt in der .env")

        _wiki = wikipediaapi.Wikipedia(
            user_agent=f"{app_name} ({contact})",
            language=language,
        )
    return _wiki



