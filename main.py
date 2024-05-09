# from menu import *
from playingcards import Deck, Card
from menu import *


def space():
    print("\n")


# Initialising a deck and set values for face cards and Aces
def starter_deck():
    deck = Deck()
    deck.shuffle()
    for card in deck:
        if card.rank == "Ace":
            card.value = 11
        elif card.rank in ["Jack", "Queen", "King"]:
            card.value = 10
    return deck


# Draw two cards from the deck for the player's starting hand
def draw_player_hand():
    deck = starter_deck()
    return [deck.draw_card(), deck.draw_card()]

# Draw two cards from the deck for the Dealers's starting hand
def draw_dealer_hand():
    deck = starter_deck()
    return [deck.draw_card(), deck.draw_card()]


# Print each card's image representation for the player's hand
def print_player_hand(hand):
    for card in hand:
        console.print(card.img, style="dodger_blue2")

def print_dealer_hand(hand):
    for card in hand:
        console.print(card.img, style="dark_red")


# Calculate the total value of the player's hand
def calculate_total(hand):
    total = sum(card.value for card in hand)
    if total >= 20:
        for card in hand:
            if card.rank == "Ace" and card.value == 11:
                card.value = 1
                total -= 10
                break
    return total


# Allow the player to take their turn in the game
def player_turn(deck, player_hand, dealer_hand):
    while True:
        print_player_hand(player_hand)
        deck.shuffle()
        total = calculate_total(player_hand)
        print(f"Your total score is: {total}")
        print_dealer_hand(dealer_hand)
        deck.shuffle()
        dealer_total = calculate_total(dealer_hand)
        print(f"Dealer's total score is: {dealer_total}")
        space()

        action = input("Hit or Stand: ").lower()
        if action == "hit" or action == 'h':
            new_card = deck.draw_card()
            player_hand.append(new_card)
            deck.shuffle()
            total += new_card.value
            space()

            if total > 21:
                print_player_hand(player_hand)
                print(f"Bust! {total} You went over 21. Dealer wins!")
                break
            elif total == 21:
                print_player_hand(player_hand)
                print("BLACKJACK! You win")
                break
        elif action == "stand":
            print("Dealer's turn.")
            while calculate_total(dealer_hand) < 17:
                new_card = deck.draw_card()
                dealer_hand.append(new_card)
                print_dealer_hand(dealer_hand)
                deck.shuffle()
            break
        else:
            # To make sure the input is valid and not something else
            print("Invalid input. Please enter 'hit' or 'stand'.")


def main():
    # Initialise the deck
    deck = starter_deck()
    # Draw the player's starting hand
    player_hand = draw_player_hand()
    # Draw the dealer's starting hand
    dealer_hand = draw_dealer_hand()
    # Allow the player to take their turn
    player_turn(deck, player_hand, dealer_hand)


# Start the game
if __name__ == "__main__":
    main()
