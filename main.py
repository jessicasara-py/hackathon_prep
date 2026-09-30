from game_logic.page_picker import pick_random_page
from menues.main_menu import main_menu
from menues.categories_menu import ask_user
from game_logic.logic import play_game
from ai_calls.statement_generator import generate_statement

MIN_VIEWS = 5000                 # Aufrufe in den letzten 30 Tagen
ROUNDS = 12


def main():
    used_titles: set[str] = set()  # bereits verwendete Seiten
    choice = main_menu()


    if choice == "1":
        category_number, menu_mapping = ask_user()

        def get_question():
            result = pick_random_page(
                menu_mapping[category_number]["name"],
                MIN_VIEWS,
                used_titles
            )

            if result is None:
                return None

            page, views = result
            return generate_statement(page.title, page.text)

        result = play_game(get_question)

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





if __name__ == "__main__":
    main()
