from rich import print
from rich.panel import Panel

logo = """
██╗    ██╗██╗██╗  ██╗██╗
██║    ██║██║██║ ██╔╝██║
██║ █╗ ██║██║█████╔╝ ██║
██║███╗██║██║██╔═██╗ ██║
╚███╔███╔╝██║██║  ██╗██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝
 """

print(logo)
print()

menue = """[blue]1. START GAME[/blue]
[blue]2. EXIT[/blue]"""

print(Panel
      (menue, width=30,
       border_style="blue",
       title="[bold yellow]TRIVIA[/bold yellow]"))

while True:
    choice = input("Your choice: ")

    if choice == "1":
        print("Starting game!")
        break

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
