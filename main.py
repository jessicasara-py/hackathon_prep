from game_logic.page_picker import pick_random_page
from api_calls.wikipedia_get_page import get_page
from menues.main_menu import main_menu
from game_logic.logic import play_game

MENU_CATEGORY = "Wissenschaft"   # erstmal statisch, siehe game_logic/categories.py
MIN_VIEWS = 5000                 # Aufrufe in den letzten 30 Tagen
ROUNDS = 3


def main():
    choice = main_menu()

    if choice == "1":
        test_questions = [
            ("Berlin ist die Hauptstadt von Deutschland.", True),
            ("Die Erde hat zwei Monde.", False),
            ("Paris liegt in Italien.", False),
        ]

        result = play_game(test_questions)

        if result == "won":
            print("Du hast gewonnen!")
        elif result == "lost":
            print("Du hast verloren!")

    elif choice == "2":
        return

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
