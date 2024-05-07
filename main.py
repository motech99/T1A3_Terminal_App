# from menu import *
from playingcards import Deck, Card
from menu import *


def space():
    print("\n")


def draw_card():
    player_deck = Deck()
    player_deck.shuffle()
    player_card = player_deck.draw_card()
    console.print(player_card.img, style="dodger_blue2")


draw_card()
draw_card()
