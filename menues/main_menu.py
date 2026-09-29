from rich import print
from rich.panel import Panel

def main_menu():
    logo = """
    ██╗    ██╗██╗██╗  ██╗██╗
    ██║    ██║██║██║ ██╔╝██║
    ██║ █╗ ██║██║█████╔╝ ██║
    ██║███╗██║██║██╔═██╗ ██║
    ╚███╔███╔╝██║██║  ██╗██║
     ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝"""

    print(logo)
    print()

    menue = """
    [blue]1. START GAME[/blue]
    [blue]2. EXIT[/blue]
    """

    print(Panel
          (menue, width=30,
           border_style="blue",
           title="[bold yellow]TRIVIA[/bold yellow]"))

    while True:
        choice = input("Your choice: ")

        if choice == "1":
            return "1"

        elif choice == "2":
            return "2"

        else:
            print("Invalid choice!")