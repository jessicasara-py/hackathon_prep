from rich.console import Console
from rich.panel import Panel

console = Console(force_terminal=True)

def main_menu():
    logo = """
    ██╗    ██╗██╗██╗  ██╗██╗
    ██║    ██║██║██║ ██╔╝██║
    ██║ █╗ ██║██║█████╔╝ ██║
    ██║███╗██║██║██╔═██╗ ██║
    ╚███╔███╔╝██║██║  ██╗██║
     ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝"""

    console.print(f"[blue]{logo}[/blue]")
    print()

    menue = """
    [blue]1. START GAME[/blue]
    [blue]2. EXIT[/blue]
    """

    console.print(Panel(
        menue,
        width=30,
        border_style="blue",
        title="[bold orange]TRICKY[/bold orange]"
    ))

    print()


    while True:
        choice = input("Your choice: ")

        if choice == "1":
            return "1"

        elif choice == "2":
            return "2"

        else:
            print("Invalid choice!")