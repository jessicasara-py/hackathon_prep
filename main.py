from game_logic.page_picker import pick_random_page
from menues.main_menu import main_menu
from menues.categories_menu import ask_user, get_article_info
from game_logic.logic import play_game
from game_logic.page_picker import get_article_info

MENU_CATEGORY = "Geography"   # erstmal statisch, siehe game_logic/categories.py
MIN_VIEWS = 5000                 # Aufrufe in den letzten 30 Tagen
ROUNDS = 3


def main():
    used_titles: set[str] = set()  # NEU: merkt sich benutzte Artikel

    choice = main_menu()

    if choice == "1":
        category_number, category_name = ask_user()
        article_info = get_article_info(int(category_number), used_titles)

        if article_info is None:
            print("Keine passende Seite gefunden.")
            return

        page, views = article_info
        print(page.title)

        test_questions = [
            {"aussage": "Berlin ist die Hauptstadt von Deutschland.", "erfunden": False},
            {"aussage": "Die Erde hat zwei Monde.", "erfunden": True},
            {"aussage": "Paris liegt in Italien.", "erfunden": True},
        ]

        result = play_game(test_questions)

        if result == "won":
            print(r"""
                   \_\_*
                 '.*==*==*=*.'
                 .-\:      /-.
                | (|:.     |) |
                 '-|:.     |-'
                   \::.    /
                    '::. .'
                      ) (
                    *.' '.*
                   `-------`
                   YOU WIN!
            """)

        elif result == "lost":
            print(r"""
               .-''''-.
              /        \
             |  X    X  |
             |          |
              \  ____  /
               '------'

               GAME OVER!
            """)

    elif choice == "2":
        return

    used_titles: set[str] = set()

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
