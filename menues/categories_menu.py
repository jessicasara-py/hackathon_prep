import wikipediaapi
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console(force_terminal=True)

# ---------------------------------------------------------
# 1. WIKIPEDIA VERBINDUNG
# ---------------------------------------------------------

wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='WikiTrivia/1.0'
)

# ---------------------------------------------------------
# 2. KATEGORIEN
# ---------------------------------------------------------

CATEGORIES = {
    1: {"name": "Geography", "wiki": "Category:Geography", "color": "red"},
    2: {"name": "History", "wiki": "Category:History", "color": "green"},
    3: {"name": "Sports", "wiki": "Category:Sports", "color": "yellow"},
    4: {"name": "Technology", "wiki": "Category:Technology", "color": "blue"},
    5: {"name": "Music", "wiki": "Category:Music", "color": "magenta"}
}


# ---------------------------------------------------------
# 3. FUNKTIONEN
# ---------------------------------------------------------

def show_menu():

    menu_text = Text()
    for number in CATEGORIES:
        info = CATEGORIES[number]
        menu_text.append(f"[{number}] {info['name']}\n", style=info["color"])

    panel = Panel(
        menu_text,
        title="CHOOSE A CATEGORY",
        border_style="bright_white",
        padding=(1, 2)
    )
    console.print(panel)

def ask_user():

    show_menu()

    while True:
        user_input = console.input("[bold cyan]Please enter a number (1-5): [/bold cyan]")

        if user_input in ["1", "2", "3", "4", "5"]:
            return int(user_input)
        else:
            console.print("[bold red]Wrong input! Please enter a number between 1 and 5.[/bold red]\n")


def get_article_info(category_number):

    category_data = CATEGORIES[category_number]
    real_name = category_data["wiki"]
    color = category_data["color"]
    display_name = category_data["name"]

    console.print(f"\n[bold {color}]Loading data for '{display_name}'...[/bold {color}] Please wait.")


    category_page = wiki.page(real_name)


    article_list = []
    for member in category_page.categorymembers.values():
        if member.ns == 0:
            article_list.append(member.title)


    if len(article_list) == 0:
        console.print("[bold red]Error: No articles found in this category![/bold red]")
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
# 4. TEST-BEREICH (NUR ZUM AUSPROBIEREN - WIRD SPÄTER ENTFERNT)
# ---------------------------------------------------------

if __name__ == "__main__":

    selected_number = ask_user()
    article_info = get_article_info(selected_number)


    if article_info is not None:
        result_text = Text()
        result_text.append("Title: ", style="bold")
        result_text.append(article_info["title"] + "\n\n")
        result_text.append("Link: ", style="bold underline blue")
        result_text.append(article_info["link"] + "\n\n")
        result_text.append("Summary:\n", style="bold")
        result_text.append(article_info["summary"])

        result_panel = Panel(
            result_text,
            title="YOUR RESULT",
            border_style="bright_green",
            padding=(1, 2)
        )
        console.print(result_panel)
    else:
        console.print("[bold red]Could not load article. Please try another categoriy![/bold red]")