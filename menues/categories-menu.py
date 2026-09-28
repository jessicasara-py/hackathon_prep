import wikipediaapi
import random

# ---------------------------------------------------------
# 1. FARBEN
# ---------------------------------------------------------

COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_RESET = "\033[0m"

# ---------------------------------------------------------
# 2. WIKIPEDIA VERBINDUNG
# ---------------------------------------------------------

wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='WikiTrivia/1.0'
)

# ---------------------------------------------------------
# 3. KATEGORIEN
# ---------------------------------------------------------

CATEGORIES = {
    1: {"name": "Geography", "wiki": "Category:Geography", "color": COLOR_RED},
    2: {"name": "History", "wiki": "Category:History", "color": COLOR_GREEN},
    3: {"name": "Sports", "wiki": "Category:Sports", "color": COLOR_YELLOW},
    4: {"name": "Technology", "wiki": "Category:Technology", "color": COLOR_BLUE},
    5: {"name": "Music", "wiki": "Category:Music", "color": COLOR_MAGENTA}
}


# ---------------------------------------------------------
# 4. FUNKTIONEN
# ---------------------------------------------------------

def show_menu():

    print("\n=== CHOOSE A CATEGORY ===")
    for number in CATEGORIES:
        info = CATEGORIES[number]
        print(f"{info['color']}[{number}] {info['name']}{COLOR_RESET}")
    print("=========================\n")


def ask_user():

    show_menu()

    while True:
        user_input = input("Please enter a number (1-5): ")

        if user_input in ["1", "2", "3", "4", "5"]:
            return int(user_input)
        else:
            print("Wrong input! Please enter a number between 1 and 5.\n")


def get_article_info(category_number):

    category_data = CATEGORIES[category_number]
    real_name = category_data["wiki"]
    color = category_data["color"]
    display_name = category_data["name"]

    print(f"\n{color}Loading data for '{display_name}'...{COLOR_RESET} Please wait.")


    category_page = wiki.page(real_name)


    article_list = []
    for member in category_page.categorymembers.values():
        if member.ns == 0:
            article_list.append(member.title)


    if len(article_list) == 0:
        print(f"{COLOR_RED}Error: No articles found in this category!{COLOR_RESET}")
        return None


    random_article_name = random.choice(article_list)


    page = wiki.page(random_article_name)


    info = {
        "title": page.title,
        "summary": page.summary,
        "link": page.fullurl
    }

    return info


# ---------------------------------------------------------
# 5. TEST-BEREICH (NUR ZUM AUSPROBIEREN - WIRD SPÄTER ENTFERNT)
# ---------------------------------------------------------

if __name__ == "__main__":

    selected_number = ask_user()
    article_info = get_article_info(selected_number)


    if article_info is not None:
        print(f"\n{COLOR_GREEN}--- YOUR RESULT ---{COLOR_RESET}")
        print("Title: " + article_info["title"])
        print("Link: " + article_info["link"])
        print("\nSummary (for your colleague):")
        print(article_info["summary"])
        print("---------------------")
    else:
        print(f"\n{COLOR_RED}Could not load article. Please try another category!{COLOR_RESET}")