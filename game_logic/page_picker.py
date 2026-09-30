import random

import wikipediaapi

from api_calls.category_cache import get_cached_category_views
from api_calls.wikipedia_get_page import get_page
from game_logic.categories import CATEGORIES, get_menu_mapping

MIN_VIEWS = 5000   # Aufrufe in den letzten 30 Tagen


def pick_random_page(
    menu_category: str,
    min_views: int,
    used_titles: set[str],
) -> tuple[wikipediaapi.WikipediaPage, int] | None:
    """
    Wählt einen zufälligen Artikel zu einer Menü-Kategorie (z. B. "Geography"), der
      - mindestens `min_views` Aufrufe in den letzten 30 Tagen hat und
      - noch nicht in `used_titles` steht.
    Der gewählte Titel wird direkt in `used_titles` eingetragen.
    Rückgabe: (page, views) oder None, wenn nichts Passendes gefunden wurde.
    """
    wiki_categories = CATEGORIES.get(menu_category)
    if not wiki_categories:
        raise ValueError(f"Unknown menu category: {menu_category}")

    # Kandidaten aus allen zugehörigen Wikipedia-Kategorien sammeln
    candidates: dict[str, int] = {}
    for wiki_category in wiki_categories:
        for title, views in get_cached_category_views(wiki_category).items():
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


def get_article_info(
    category_number: int,
    used_titles: set[str],
) -> tuple[wikipediaapi.WikipediaPage, int] | None:
    """Menü-Nummer (1, 2, 3 …) → zufälliger Artikel. Rückgabe: (page, views) oder None."""
    mapping = get_menu_mapping()
    menu_name = mapping[category_number]["name"]
    return pick_random_page(menu_name, MIN_VIEWS, used_titles)