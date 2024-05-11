from playingcards import Deck
from menu import *

"""playingcards: Creating, shuffling, and displaying decks made easier with this Python Playing Card Module."""


class Score:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self. ties = 0

    def scoreboard(self):
        console.print(
            f"Wins: {
                self.wins} Losses: {
                self.losses} Ties: {
                self.ties}",
            style="dark_violet bold")


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
def draw_cards():
    deck = starter_deck()
    return [deck.draw_card(), deck.draw_card()]


# Print each card's image representation for the player's hand
def print_hand(hand, color):
    for card in hand:
        console.print(card.img, style=color)


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
def turn(deck, player_hand, dealer_hand, score):
    while True:
        print_hand(player_hand, "dodger_blue2")
        total = calculate_total(player_hand)
        print(f"Your total score is: {total}")

        print_hand(dealer_hand, "purple4")
        dealer_total = calculate_total(dealer_hand)
        print(f"Dealer's total score is: {dealer_total}")
        print_blank_line()

        # Player's turn
        action = input("Hit or stand: ").strip().lower()
        if action == "hit":

            new_card = deck.draw_card()
            player_hand.append(new_card)
            total += new_card.value
            print_blank_line()

            if total > 21:
                print_hand(player_hand, "dodger_blue2")
                print(f"Bust! {total} You went over 21. Dealer wins!")
                score.losses += 1
                return
            elif total == 21:
                print_hand(player_hand, "dodger_blue2")
                console.print("BLACKJACK! You win", style="green3")
                score.wins += 1
                return

        elif action == "stand":
            print("Dealer's turn.")

            # Dealers Turn
            while calculate_total(dealer_hand) < 17:
                new_card = deck.draw_card()
                dealer_hand.append(new_card)
                print_hand(dealer_hand, "purple4")
                dealer_total += new_card.value
                print(f"Dealer's total score is: {dealer_total}")
                print_blank_line()

                if dealer_total > 21:
                    print(
                        f"Bust! {dealer_total} Dealer went over 21. You win!")
                    score.wins += 1
                    return
                elif dealer_total == 21:
                    print_hand(dealer_hand, "purple4")
                    print("BLACKJACK! Dealer wins")
                    return

            # Check if the game has reached a conclusion
            if dealer_total >= 17:
                # Compare scores and determine the winner
                if total > dealer_total and total <= 21:
                    print_hand(player_hand, "dodger_blue2")
                    print("You win!")
                    score.wins += 1
                elif dealer_total > total and dealer_total <= 21:
                    print_hand(dealer_hand, "purple4")
                    console.print(
                        f"[dodger_blue1 bold]Your score: [underline]{
                            total}[/][/] [slate_blue3 bold] dealer's score: [underline]{dealer_total}[/][/]"
                    )
                    print_blank_line()
                    print("Dealer wins!")
                    score.losses += 1
                else:
                    print("It's a tie!")
                    score.ties += 1
                return

        else:
            # To make sure the input is valid and not something else
            console.print(
                "Invalid input. Please enter 'hit' or 'stand'.",
                style="red1")


def ask_play_again():
    while True:
        play_again = input(
            "Do you want to play again? (yes/no): ").strip().lower()
        if play_again in ["yes", "no"]:
            return play_again
        else:
            console.print(
                "Error: Invalid input. Please enter 'yes' or 'no'.",
                style="red")


def main():
    score = Score()
    while True:
        try:
            # Initialise the scoreboard
            score.scoreboard()
            # Initialise the deck
            deck = starter_deck()
            # Draw the player's starting hand
            player_hand = draw_cards()
            # Draw the dealer's starting hand
            dealer_hand = draw_cards()
            # Allow the player/dealerto take their turn
            turn(deck, player_hand, dealer_hand, score)

            play_again = ask_play_again()
            if play_again == "no":
                end_title = "Thanks for playing!"
                game_end_title = figlet_format(end_title)
                console.print(game_end_title, style="dark_magenta")
                score.scoreboard()
                break

        except ValueError as ve:
            console.print("Error:", ve, style="red")
        except IOError as ioe:
            console.print("IOError:", ioe, style="red")


# Start the game
if __name__ == "__main__":
    main()
