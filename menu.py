# Third-party imports
from rich.console import Console
from pyfiglet import figlet_format


console = Console()
game_title = "Blackjack"
title = figlet_format(game_title)

console.print(title, style="blue_violet")
console.print(
    "Hello! Thank you for checking out my game of Blackjack! Hope you Enjoy! \n")


# a function to raise errors if name is empty string or is a number
def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty")
    if not name.isalpha():
        raise ValueError(
            "Name can only contain alphabetic characters"
        )


# loops name variable and prints appropriate error until inputs a valid
# name (string)
while True:
    try:
        name = input("Enter your name to play: ").lower()
        validate_name(name)
        console.print("Welcome!", name, style='green')
        break
    except ValueError as e:
        console.print("Error:", e, style='red')
    except TypeError as e:
        print("Error:", e,)
