# from menu import *
from playingcards import Deck, Card
from menu import *


def space():
    print("\n")

player_score = 0

deck = Deck()
for card in deck:
    if card.rank == 'Ace':
        card.value = 11
    elif card.rank == 'Jack' or card.rank == 'Queen' or card.rank == 'King':
        card.value = 10

def draw_card():
    deck.shuffle()
    player_card = deck.draw_card()
    console.print(player_card.img, style="dodger_blue2")
    print(player_card.value)




draw_card()
draw_card()



