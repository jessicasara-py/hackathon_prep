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
        "World War II"
    ],
    "Sports": [
        "Olympic Games",
        "Sports",
        "Association football"
    ],
    "Technology": [
        "Computer science",
        "Artificial intelligence",
        "Software"
    ],
    "Music": [
        "Albums",
        "Songs",
        "Musical instruments"
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

