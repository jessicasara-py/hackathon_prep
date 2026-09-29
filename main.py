from api_calls.wikipedia_get_page import get_page
from menues.main_menu import main_menu
from menues.categories_menu import ask_user, get_article_info
from game_logic.logic import play_game

def main():
    choice = main_menu()

    if choice == "1":
        category_number = ask_user()
        article_info = get_article_info(category_number)

        print(article_info)

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

    page = get_page("Augsburg")
    print(page.summary[:300] if page else "Seite nicht gefunden")


if __name__ == '__main__':
    main()
