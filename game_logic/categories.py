"""
Menü-Kategorien → echte Wikipedia-Kategorien.

Oberkategorien wie "Wissenschaft" enthalten fast nur Unterkategorien.
Deshalb bildet jeder Menüpunkt auf mehrere konkrete Kategorien ab,
die direkt viele Artikel enthalten.

Prüfen mit:  python -m game_logic.categories
(füllt dabei auch den Cache – ideal vor einer Demo)
"""

CATEGORIES: dict[str, list[str]] = {
    "Geography": [
        "Countries",
        "Mountains",
        "Rivers"
    ],
    "History": [
        "Ancient history",
        "20th century",
        "Historical events"
    ],
    "Sports": [
        "Footballers",
        "Olympic medalists",
        "Tennis players"
    ],
    "Technology": [
        "Computer science",
        "Artificial intelligence",
        "Software"
    ],
    "Music": [
        "Rock music groups",
        "Classical composers",
        "Singers"
    ]
}


def get_menu_mapping() -> dict[int, dict]:
    """
    Wandelt das CATEGORIES Dictionary in das Format um,
    das das Menü (categories_menu.py) für die Anzeige braucht.
    """
    menu_mapping = {}
    colors = ["red", "green", "yellow", "blue", "magenta"]

    for i, (name, wiki_cats) in enumerate(CATEGORIES.items(), start=1):
        menu_mapping[i] = {
            "name": name,
            "api_names": wiki_cats,  # Die Liste der echten Wiki-Kategorien
            "color": colors[i - 1]
        }
    return menu_mapping


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
