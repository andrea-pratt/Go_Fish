import random 
import dataclasses

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# There will be two players in this game. The user, and the computer
class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = []


def create_deck():
    deck = cards*4
    random.shuffle(deck)
    print(deck)
    print(len(deck))

create_deck()