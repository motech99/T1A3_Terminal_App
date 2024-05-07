from rich.console import Console
from pyfiglet import figlet_format


console = Console()
game_title = "Blackjack"
title = figlet_format(game_title)

console.print(title, style="blue_violet")
console.print("Hello! Thank you for checking out my game of Blackjack! Hope you Enjoy!")


def validate_name(name):
    if not name:
        raise ValueError("Name  cannot be empty")
    if not isinstance(name, str):
        raise TypeError("Name must  be a string")
    if not name.isalpha():
        raise ValueError("Name can only contain alphabetic characters")


while True:
    try:
        name = input("Enter your name: ")
        validate_name(name)
        print("Name is valid:", name)
        break
    except ValueError as e:
        print("Error:", e)
    except TypeError as e:
        print("Error:", e)
