# from menu import *
from playingcards import Deck, Card
from menu import *


def space():
    print("\n")

deck = Deck()
for card in deck:
    if card.rank == 'Ace':
        card.value = 11
    elif card.rank == 'Jack' or card.rank == 'Queen' or card.rank == 'King':
        card.value = 10

def draw_card():
    deck.shuffle()
    card = deck.draw_card()
    console.print(card.img, style="dodger_blue2")
    return card


player_hand = []

total = 0
for card in player_hand:
    total += card.value
print(total)
    





