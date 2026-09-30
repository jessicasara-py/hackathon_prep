from api_calls.wiki_client import get_wiki

ARTICLE_NAMESPACE = 0  # 0 = normale Artikel (keine Unterkategorien, Dateien, Vorlagen)


def get_category_articles(category: str) -> list[str]:
    """Liefert die Titel aller Artikel einer Kategorie (ohne Unterkategorien)."""
    if not category.startswith("Kategorie:"):
        category = f"Kategorie:{category}"

    cat = get_wiki().page(category)
    if not cat.exists():
        return []

    return [
        title
        for title, member in cat.categorymembers.items()
        if member.ns == ARTICLE_NAMESPACE
    ]
