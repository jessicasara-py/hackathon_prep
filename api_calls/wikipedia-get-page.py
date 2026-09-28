from api_calls.wiki_client import get_wiki


def get_page(title: str):
    page = get_wiki().page(title)
    return page if page.exists() else None

""" 
zum testen statischer aufruf
page.summary[:300] -> holt die ersten 300 Zeichen
"""

page = get_page("Augsburg")
print(page.summary[:300] if page else "Seite nicht gefunden")