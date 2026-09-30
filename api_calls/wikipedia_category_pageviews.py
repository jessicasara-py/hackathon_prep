import requests

from api_calls.wiki_client import get_language, get_user_agent


def get_category_articles_with_views(category: str, days: int = 30) -> dict[str, int]:
    """
    Holt alle Artikel einer Kategorie inkl. Seitenaufrufen der letzten `days` Tage
    (max. 60) über die Action API – statt einem Pageviews-Call pro Artikel.

    Rückgabe: {"Titel": Aufrufe, ...}
    """
    if not category.startswith("category:"):
        category = f"category:{category}"

    url = f"https://{get_language()}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "categorymembers",
        "gcmtitle": category,
        "gcmtype": "page",        # nur Artikel, keine Unterkategorien
        "gcmlimit": "max",
        "prop": "pageviews",
        "pvipdays": days,
        "format": "json",
        "formatversion": 2,       # "pages" kommt als Liste statt als Dict
    }
    headers = {"User-Agent": get_user_agent()}

    views: dict[str, int] = {}
    cont: dict = {}

    # Die API liefert große Ergebnisse in Teilen ("continue").
    # Wir fragen so lange nach, bis kein "continue" mehr kommt.
    while True:
        response = requests.get(url, params={**params, **cont}, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            raise RuntimeError(
                f"Wikipedia-API-Error for '{params['gcmtitle']}' "
                f"({url}): {data['error'].get('info')}"
            )

        for page in data.get("query", {}).get("pages", []):
            daily = page.get("pageviews") or {}
            # Tage ohne Daten kommen als None → als 0 zählen
            total = sum(v for v in daily.values() if v)
            # Pageviews können in mehreren Teilantworten kommen → aufaddieren
            views[page["title"]] = views.get(page["title"], 0) + total

        if "continue" not in data:
            break
        cont = data["continue"]

    return views


