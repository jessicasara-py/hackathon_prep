import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from api_calls.wikipedia_check_categories import get_category_articles
from api_calls.wiki_client import get_wiki

# ---------------------------------------------------------
# 1. RICH KONSOLE
# ---------------------------------------------------------
console = Console(force_terminal=True)

# ---------------------------------------------------------
# 2. KATEGORIEN
# ---------------------------------------------------------

CATEGORIES = {
    1: {"name": "Geography", "api_name": "Geography", "color": "red"},
    2: {"name": "History", "api_name": "History", "color": "green"},
    3: {"name": "Sports", "api_name": "Sports", "color": "yellow"},
    4: {"name": "Technology", "api_name": "Technology", "color": "blue"},
    5: {"name": "Music", "api_name": "Music", "color": "magenta"}
}

# ---------------------------------------------------------
# 3. MENÜ FUNKTIONEN
# ---------------------------------------------------------

def show_menu():
    """Zeigt das nummerierte Menü in einer schönen Box an."""
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
    """Fragt den User nach einer Nummer von 1 bis 5."""
    show_menu()

    while True:
        user_input = console.input("[bold cyan]Please enter a number (1-5): [/bold cyan]")

        if user_input in ["1", "2", "3", "4", "5"]:
            return int(user_input)
        else:
            console.print("[bold red]Wrong input! Please enter a number between 1 and 5.[/bold red]\n")


def get_article_info(category_number):
    """
    Holt die Liste der Artikel von (API-CALLS), wählt einen zufälligen
    und holt dann die Details (Titel, Link, Summary).
    """
    category_data = CATEGORIES[category_number]
    api_name = category_data["api_name"]
    color = category_data["color"]

    console.print(f"\n[bold {color}]Loading data for '{category_data['name']}'...[/bold {color}] Please wait.")

    # 1. Nutzt die funktion con (API-CALLS), um alle Artikel zu holen
    article_list = get_category_articles(api_name)

    # Prüfen ob die liste leer ist
    if not article_list:
        console.print("[bold red]Error: No articles found in this category![/bold red]")
        return None

    # 2. Wählt einen zufälligen Artikel aus der Liste
    random_article_name = random.choice(article_list)

    # 3. Holt die genauen Infos über den zentralen Wiki-Client
    wiki = get_wiki()
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
        console.print("[bold red]Could not load article. Please try another category![/bold red]")