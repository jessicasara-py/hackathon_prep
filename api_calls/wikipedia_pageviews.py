from datetime import date, timedelta
from urllib.parse import quote

import requests

from api_calls.wiki_client import get_language, get_user_agent

PAGEVIEWS_URL = (
    "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
    "{project}/all-access/user/{article}/daily/{start}/{end}"
)


def get_pageviews(title: str, days: int = 30) -> int:
    """Summe der Seitenaufrufe (nur echte Nutzer, keine Bots) der letzten `days` Tage."""
    end = date.today() - timedelta(days=1)          # heute ist noch nicht vollständig
    start = end - timedelta(days=days - 1)

    url = PAGEVIEWS_URL.format(
        project=f"{get_language()}.wikipedia",
        article=quote(title.replace(" ", "_"), safe=""),
        start=start.strftime("%Y%m%d"),
        end=end.strftime("%Y%m%d"),
    )

    response = requests.get(url, headers={"User-Agent": get_user_agent()}, timeout=10)
    if response.status_code == 404:                 # keine Daten für diesen Artikel
        return 0
    response.raise_for_status()

    return sum(item["views"] for item in response.json().get("items", []))

