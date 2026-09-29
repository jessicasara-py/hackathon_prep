import random

import wikipediaapi

from api_calls.wikipedia_category_pageviews import get_category_articles_with_views
from api_calls.wikipedia_get_page import get_page
from game_logic.categories import CATEGORIES

# Zwischenspeicher: Kategorie → {Titel: Aufrufe}
# Damit wird jede Kategorie pro Spiel nur einmal von der API geladen.
_views_cache: dict[str, dict[str, int]] = {}


def _get_views(wiki_category: str) -> dict[str, int]:
    if wiki_category not in _views_cache:
        _views_cache[wiki_category] = get_category_articles_with_views(wiki_category)
    return _views_cache[wiki_category]


def pick_random_page(
    menu_category: str,
    min_views: int,
    used_titles: set[str],
) -> tuple[wikipediaapi.WikipediaPage, int] | None:
    """
    Wählt einen zufälligen Artikel zu einer Menü-Kategorie (z. B. "Wissenschaft"), der
      - mindestens `min_views` Aufrufe in den letzten 30 Tagen hat und
      - noch nicht in `used_titles` steht.
    Der gewählte Titel wird direkt in `used_titles` eingetragen.
    Rückgabe: (page, views) oder None, wenn nichts Passendes gefunden wurde.
    """
    wiki_categories = CATEGORIES.get(menu_category)
    if not wiki_categories:
        raise ValueError(f"Unbekannte Menü-Kategorie: {menu_category}")

    # Kandidaten aus allen zugehörigen Wikipedia-Kategorien sammeln
    candidates: dict[str, int] = {}
    for wiki_category in wiki_categories:
        for title, views in _get_views(wiki_category).items():
            if views >= min_views and title not in used_titles:
                candidates[title] = views

    if not candidates:
        return None

    title = random.choice(list(candidates))
    page = get_page(title)
    if page is None:
        return None

    used_titles.add(title)
    return page, candidates[title]
