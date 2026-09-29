from api_calls.wikipedia_get_page import get_page
from menues.main_menu import main_menu
from game_logic.logic import play_game


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

    page = get_page("Augsburg")
    print(page.summary[:300] if page else "Seite nicht gefunden")

if __name__ == '__main__':
    main()
