# from menu import *
from playingcards import Deck, Card
from menu import *


def space():
    print("\n")

# Initialising a deck and set values for face cards and Aces


def starter_deck():
    deck = Deck()
    for card in deck:
        if card.rank == "Ace":
            card.value = 11
        elif card.rank in ["Jack", "Queen", "King"]:
            card.value = 10
    return deck

 # Draw two cards from the deck for the player's starting hand


def draw_hand(deck):
    return [deck.draw_card(), deck.draw_card()]

 # Print each card's image representation for the player's hand


def print_hand(hand):
    for card in hand:
        console.print(card.img, style="dodger_blue2")

# Calculate the total value of the player's hand


def calculate_total(hand):
    return sum(card.value for card in hand)

# Allow the player to take their turn in the game


def player_turn(deck, player_hand):
    while True:
        print_hand(player_hand)
        total = calculate_total(player_hand)
        print(f"Your total score is: {total}")
        space()

        action = input("Hit or Stand: ").lower()
        if action == "hit":
            new_card = deck.draw_card()
            player_hand.append(new_card)
            total += new_card.value
            print(f"Your total score is now: {total}")
            space()

            if total > 21:
                print_hand(player_hand)
                print("Bust! You went over 21. Dealer wins!")
                break
            elif total == 21:
                print("Blackjack! You win")
                break
        elif action == "stand":
            print("You chose to stand.")
            break
        else:
            # To make sure the input is valid and not something else
            print("Invalid input. Please enter 'hit' or 'stand'.")


def main():
    # Initialise the deck
    deck = starter_deck()
    # Draw the player's starting hand
    player_hand = draw_hand(deck)
    # Allow the player to take their turn
    player_turn(deck, player_hand)


# Start the game
if __name__ == "__main__":
    main()
