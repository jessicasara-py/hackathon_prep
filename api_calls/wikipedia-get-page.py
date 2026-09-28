from api_calls.wiki_client import get_wiki


def get_page(title: str):
    page = get_wiki().page(title)
    return page if page.exists() else None