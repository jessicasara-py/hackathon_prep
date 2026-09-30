from game_logic.page_picker import pick_random_page
from menues.main_menu import main_menu
from menues.categories_menu import ask_user, get_article_info
from game_logic.logic import play_game
from game_logic.page_picker import get_article_info
from ai_calls.statement_generator import generate_statement

MENU_CATEGORY = "Geography"   # erstmal statisch, siehe game_logic/categories.py
ROUNDS = 3
MAX_ATTEMPTS = 6    # so viele Artikel probieren wir höchstens, falls die KI mal scheitert

def build_questions(category_number: int, used_titles: set[str]) -> list[dict]:
    """
    Erzeugt ROUNDS Quizfragen aus zufälligen Wikipedia-Artikeln der gewählten Kategorie.
    Jede Frage: {"aussage": str, "erfunden": bool, "erklaerung": str, "titel": str}
    """
    questions: list[dict] = []

    for _ in range(MAX_ATTEMPTS):
        if len(questions) >= ROUNDS:
            break

        article_info = get_article_info(category_number, used_titles)
        if article_info is None:
            break                          # keine Artikel mehr in der Kategorie

        page, _ = article_info
        print(f"  … Frage {len(questions) + 1}/{ROUNDS} wird erstellt ({page.title})")

        try:
            statement = generate_statement(page.title, page.text)
        except Exception as error:         # KI-Fehler → nächsten Artikel probieren
            print(f"  ! Übersprungen: {error}")
            continue

        statement["titel"] = page.title
        questions.append(statement)

    return questions


def ask_name():
    name = input("What is your name? ")
    print(f"\nWelcome, {name}, to...\n")
    return name


def main():
    used_titles: set[str] = set()  # bereits verwendete Seiten
    name = ask_name()
    choice = main_menu()

    if choice == "1":
        category_number, menu_mapping = ask_user()
        category_name = menu_mapping[int(category_number)]["name"]

        print(f"\nFragen zu '{category_name}' werden vorbereitet …")
        questions = build_questions(int(category_number), used_titles)

        if not questions:
            print("Keine passende Seite gefunden.")
            return

        result = play_game(questions)

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
