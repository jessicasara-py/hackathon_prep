from rich.console import Console
from rich import print
from rich.panel import Panel
from ai_calls.statement_generator import generate_statement
from game_logic.logic import play_game
from game_logic.page_picker import pick_random_page
from menues.categories_menu import ask_user
from menues.main_menu import main_menu

console = Console()

MIN_VIEWS = 5000     # Aufrufe in den letzten 30 Tagen
MAX_ATTEMPTS = 3     # so viele Artikel pro Frage probieren, falls die KI scheitert


def make_get_question(category_name: str, used_titles: set[str]):
    """Liefert eine Funktion, die bei jedem Aufruf genau EINE neue Frage erzeugt."""

    def get_question():
        for _ in range(MAX_ATTEMPTS):
            result = pick_random_page(category_name, MIN_VIEWS, used_titles)
            if result is None:
                return None                     # Kategorie erschöpft
            page, _ = result
            print(f"  … Question is being generated ({page.title})")

            try:
                statement = generate_statement(page.title, page.text)
            except Exception as error:          # KI-Fehler → nächsten Artikel probieren
                print(f"  ! Skipped: {error}")
                continue

            statement["titel"] = page.title
            return statement

        return None

    return get_question


def ask_name():
    name = console.input("[bold cyan]What is your name? [/bold cyan]").strip()

    print(Panel(
        f"Welcome, {name}!",
        title="[orange1]WIKITRICKY[/orange1]",
        border_style="cyan",
        width=30
    ))
    return name


def main():

    used_titles: set[str] = set()  # bereits verwendete Seiten
    name = ask_name()



    while True: # Schleife für "Nochmal spielen?"
        choice = main_menu()

        if choice == "2":
            print("Goodbye!")
            break # Schleife beendet

        while True:
            category_number, menu_mapping = ask_user()
            category_name = menu_mapping[int(category_number)]["name"]

            print(f"\nQuiz for '{category_name}' is starting …")
            result = play_game(make_get_question(category_name, used_titles))


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

            elif result == "invalid_input":
                print("\n  Game aborted: three invalid inputs.")

            elif result == "not_enough_questions":
                print("\n  No more questions available in this category.")
                print("  Tip: choose another category or lower MIN_VIEWS.")
            else:
                print(f"\n  Unexpected result: {result}")

            # NEU: Frage ob nochmal spielen
            print("\n" + "="*40)
            play_again = console.input("[orange1]Do you want to play again? [Y/N]: [/orange1]").strip().lower()

            if play_again not in ("y", "yes"):
                print("Thanks for playing! See you next time!")
                return # Schleife beendet

            print("\n" + "="*40 + "\n")
            used_titles.clear() # Setzt die verwendeten Titel für das nächste Spiel zurück


if __name__ == "__main__":
    main()