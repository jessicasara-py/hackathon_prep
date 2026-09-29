import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from categories import get_menu_mapping
from api_calls.wikipedia_check_categories import get_category_articles
from api_calls.wiki_client import get_wiki

console = Console()


def show_menu():
    """Zeigt das nummerierte Menü in einer schönen Box an."""
    menu_mapping = get_menu_mapping()  # Holt die Daten zentral!

    menu_text = Text()
    for number, info in menu_mapping.items():
        menu_text.append(f"[{number}] {info['name']}\n", style=info["color"])

    panel = Panel(
        menu_text,
        title="CHOOSE A CATEGORY",
        border_style="bright_white",
        padding=(1, 2)
    )
    console.print(panel)
    return menu_mapping


def ask_user():
    """Fragt den User nach einer Nummer von 1 bis 5."""
    menu_mapping = show_menu()

    while True:
        user_input = console.input("[bold cyan]Please enter a number (1-5): [/bold cyan]")

        if user_input in ["1", "2", "3", "4", "5"]:
            return int(user_input), menu_mapping
        else:
            console.print("[bold red]Wrong input! Please enter a number between 1 and 5.[/bold red]\n")


def get_article_info(category_number, menu_mapping):
    """Holt die Liste der Artikel, wählt einen zufälligen und holt die Details."""
    category_data = menu_mapping[category_number]
    api_names = category_data["api_names"]  # Das ist jetzt eine LISTE von Kategorien!
    color = category_data["color"]
    display_name = category_data["name"]

    console.print(f"\n[bold {color}]Loading data for '{display_name}'...[/bold {color}] Please wait.")

    primary_category = api_names[0]

    article_list = get_category_articles(primary_category)

    if not article_list:
        console.print("[bold red]Error: No articles found in this category![/bold red]")
        return None

    random_article_name = random.choice(article_list)
    wiki = get_wiki()
    page = wiki.page(random_article_name)

    return {
        "title": page.title,
        "summary": page.summary,
        "link": page.fullurl
    }


# TEST-BEREICH
if __name__ == "__main__":
    selected_number, mapping = ask_user()
    article_info = get_article_info(selected_number, mapping)

    if article_info is not None:
        result_text = Text()
        result_text.append("Title: ", style="bold")
        result_text.append(article_info["title"] + "\n\n")
        result_text.append("Link: ", style="bold underline blue")
        result_text.append(article_info["link"] + "\n\n")
        result_text.append("Summary:\n", style="bold")
        result_text.append(article_info["summary"][:400] + "...")

        result_panel = Panel(
            result_text,
            title="YOUR RESULT",
            border_style="bright_green",
            padding=(1, 2)
        )
        console.print(result_panel)
    else:
        console.print("[bold red]Could not load article. Please try another category![/bold red]")