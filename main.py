# from menu import *
from playingcards import Deck, Card
from menu import *


def space():
    print("\n")


deck = Deck()
for card in deck:
    if card.rank == "Ace":
        card.value = 11
    elif card.rank == "Jack" or card.rank == "Queen" or card.rank == "King":
        card.value = 10


def draw_card():
    deck.shuffle()
    card = deck.draw_card()
    console.print(card.img, style="dodger_blue2")
    return card


player_hand = [draw_card(), draw_card()]


while True:
    total = 0
    for card in player_hand:
        total += card.value

    print(f'your total score is: {total}')
    space()

    action = input("Hit or Stand: ").lower()
    if action == "Hit".lower():
        new_card = draw_card()
        player_hand.append(new_card)
        total += new_card.value
        print(f'Your total score is now: {total}')
        space() 

        if total > 21:
            print("Bust! You went over 21. Dealer wins!")
            break  
        
    elif action == "stand":
        print("You chose to stand.")
        break  
    else:
        print("Invalid input. Please enter 'hit' or 'stand'.")
