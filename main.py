from api_calls.wikipedia_get_page import get_page


def main():
    page = get_page("Augsburg")
    print(page.summary[:300] if page else "Seite nicht gefunden")

if __name__ == '__main__':
    main()
