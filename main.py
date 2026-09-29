from game_logic.page_picker import pick_random_page

MENU_CATEGORY = "Wissenschaft"   # erstmal statisch, siehe game_logic/categories.py
MIN_VIEWS = 5000                 # Aufrufe in den letzten 30 Tagen
ROUNDS = 3


def main():
    used_titles: set[str] = set()    # bereits verwendete Seiten

    for round_no in range(1, ROUNDS + 1):
        result = pick_random_page(MENU_CATEGORY, MIN_VIEWS, used_titles)
        if result is None:
            print("Keine passende Seite gefunden.")
            break

        page, views = result
        print(f"\n--- Frage {round_no}: {page.title} ({views} Aufrufe / 30 Tage) ---")
        print(page.summary[:300])

    print(f"\nBereits verwendet: {sorted(used_titles)}")


if __name__ == "__main__":
    main()
