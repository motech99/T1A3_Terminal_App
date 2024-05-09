from playingcards import Deck
from menu import *

"""playingcards: Creating, shuffling, and displaying decks made easier with this Python Playing Card Module."""


def print_blank_line():
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
        console.print(card.img, style="purple4")


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


# Turn Mechanic for player and dealer
def turn(deck, player_hand, dealer_hand):
    while True:
        print_player_hand(player_hand)
        total = calculate_total(player_hand)
        print(f"Your total score is: {total}")

        print_dealer_hand(dealer_hand)
        dealer_total = calculate_total(dealer_hand)
        print(f"Dealer's total score is: {dealer_total}")
        print_blank_line()

        # Player's turn
        action = input("hit or stand: ").lower()
        if action == "hit":

            new_card = deck.draw_card()
            player_hand.append(new_card)
            total += new_card.value
            print_blank_line()

            if total > 21:
                print_player_hand(player_hand)
                print(f"Bust! {total} You went over 21. Dealer wins!")
                return
            elif total == 21:
                print_player_hand(player_hand)
                console.print("BLACKJACK! You win", style="green3")
                return

        elif action == "stand":
            print("Dealer's turn.")

            # Dealers Turn
            while calculate_total(dealer_hand) < 17:
                new_card = deck.draw_card()
                dealer_hand.append(new_card)
                print_dealer_hand(dealer_hand)
                dealer_total += new_card.value
                print(f"Dealer's total score is: {dealer_total}")
                print_blank_line()

                if dealer_total > 21:
                    print(f"Bust! {dealer_total} Dealer went over 21. You win!")
                    return
                elif dealer_total == 21:
                    print_dealer_hand(dealer_hand)
                    print("BLACKJACK! Dealer wins")
                    return

            # Check if the game has reached a conclusion
            if dealer_total >= 17:
                # Compare scores and determine the winner
                if total > dealer_total and total <= 21:
                    print_player_hand(player_hand)
                    print("You win!")
                elif dealer_total > total and dealer_total <= 21:
                    print_dealer_hand(dealer_hand)
                    console.print(
                        f"[dodger_blue1 bold]Your score: [underline]{total}[/][/] [slate_blue3 bold] dealer's score: [underline]{dealer_total}[/][/]"
                    )
                    print_blank_line()
                    print("Dealer wins!")
                else:
                    print("It's a tie!")
                return

        else:
            # To make sure the input is valid and not something else
            console.print("Invalid input. Please enter 'hit' or 'stand'.", style="red1")


def main():
    while True:
        # Initialise the deck
        deck = starter_deck()
        # Draw the player's starting hand
        player_hand = draw_player_hand()
        # Draw the dealer's starting hand
        dealer_hand = draw_dealer_hand()
        # Allow the player/dealerto take their turn
        turn(deck, player_hand, dealer_hand)
        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            end_title = "Thanks for playing!"
            game_end_title = figlet_format(end_title)
            console.print(game_end_title, style="dark_magenta")
            break


# Start the game
if __name__ == "__main__":
    main()
