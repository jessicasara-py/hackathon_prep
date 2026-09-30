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

    console.print(f"[cyan]{logo}[/cyan]")
    print()

    menue = """
    [cyan]1. START GAME[/cyan]
    [cyan]2. EXIT[/cyan]
    """

    console.print(Panel(
        menue,
        width=30,
        border_style="cyan",
        title="[bold orange1]TRICKY[/bold orange1]"
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