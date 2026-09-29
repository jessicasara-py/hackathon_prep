"""
Datei-Cache für Kategorie-Artikel inkl. Seitenaufrufe.

Ablauf bei get_cached_category_views("Chemisches Element"):
  1. Im Arbeitsspeicher?          → sofort zurück
  2. JSON-Datei in cache/ aktuell? → laden, zurück
  3. Sonst: API abfragen, als JSON speichern, zurück

Cache leeren: einfach den Ordner cache/ löschen.
"""
import json
import re
from datetime import date
from pathlib import Path

from api_calls.wiki_client import get_language
from api_calls.wikipedia_category_pageviews import get_category_articles_with_views

CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"   # <Projekt-Root>/cache
CACHE_MAX_AGE_DAYS = 1   # 1 = einmal pro Tag neu laden

_memory: dict[str, dict[str, int]] = {}


def _cache_file(category: str) -> Path:
    # Dateiname ohne Sonderzeichen, z. B. "de_Fußballnationalspieler_Deutschland_.json"
    safe_name = re.sub(r"[^\w\-]+", "_", category)
    return CACHE_DIR / f"{get_language()}_{safe_name}.json"


def _load_from_file(path: Path) -> dict[str, int] | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        age = (date.today() - date.fromisoformat(data["fetched_at"])).days
        if age >= CACHE_MAX_AGE_DAYS:
            return None                      # zu alt → neu laden
        return data["views"]
    except (json.JSONDecodeError, KeyError, ValueError):
        return None                          # Datei kaputt → neu laden


def _save_to_file(path: Path, category: str, views: dict[str, int]) -> None:
    CACHE_DIR.mkdir(exist_ok=True)
    data = {
        "category": category,
        "language": get_language(),
        "fetched_at": date.today().isoformat(),
        "views": views,
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def get_cached_category_views(category: str) -> dict[str, int]:
    """Wie get_category_articles_with_views(), aber mit Speicher- und Datei-Cache."""
    if category in _memory:
        return _memory[category]

    path = _cache_file(category)
    views = _load_from_file(path)

    if views is None:
        views = get_category_articles_with_views(category)
        _save_to_file(path, category, views)

    _memory[category] = views
    return views
