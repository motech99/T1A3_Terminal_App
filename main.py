# from menu import *
from playingcards import Deck, Card
from menu import *


def space():
    print("\n")


def starter_deck():
    deck = Deck()
    for card in deck:
        if card.rank == "Ace":
            card.value = 11
        elif card.rank in ["Jack", "Queen", "King"]:
            card.value = 10
    return deck


def draw_hand(deck):
    return [deck.draw_card(), deck.draw_card()]


def print_hand(hand):
    for card in hand:
        console.print(card.img, style="dodger_blue2")


def calculate_total(hand):
    return sum(card.value for card in hand)


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
            print("Invalid input. Please enter 'hit' or 'stand'.")


def main():
    deck = starter_deck()
    player_hand = draw_hand(deck)
    player_turn(deck, player_hand)


if __name__ == "__main__":
    main()
