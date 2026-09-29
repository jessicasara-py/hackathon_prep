"""
Menü-Kategorien → echte Wikipedia-Kategorien.

Oberkategorien wie "Wissenschaft" enthalten fast nur Unterkategorien.
Deshalb bildet jeder Menüpunkt auf mehrere konkrete Kategorien ab,
die direkt viele Artikel enthalten.

Prüfen mit:  python -m game_logic.categories
(füllt dabei auch den Cache – ideal vor einer Demo)
"""

CATEGORIES: dict[str, list[str]] = {
    "Wissenschaft": [
        "Chemisches Element",
        "Nobelpreisträger für Physik",
        "Nobelpreisträger für Chemie",
    ],
    "Geographie": [
        "Hauptstadt in Europa",
        "Mitgliedstaat der Europäischen Union",
    ],
    "Sport": [
        "Fußballnationalspieler (Deutschland)",
        "Fußballweltmeister (Deutschland)",
    ],
}


def _demo():
    # Zeigt pro Kategorie, wie viele Artikel sie hat und wie viele genug Aufrufe haben.
    from api_calls.category_cache import get_cached_category_views

    min_views = 5000
    for menu, wiki_categories in CATEGORIES.items():
        print(f"\n== {menu} ==")
        for cat in wiki_categories:
            views = get_cached_category_views(cat)
            popular = sum(1 for v in views.values() if v >= min_views)
            status = "OK " if popular else "!! "
            print(f"  {status}{cat}: {len(views)} Artikel, {popular} mit >= {min_views} Aufrufen")


if __name__ == "__main__":
    _demo()
