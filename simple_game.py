import random 
import dataclasses

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []

# There will be two players in this game. The user, and the computer
class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = []


# This function creates a shuffled deck with 52 cards
def create_deck():
    deck = cards*4
    random.shuffle(deck)
    return deck


def initialize_players():
    print('do stuff here')
    


def deal_hand(deck):
    hand = []
    for _ in range(7):
        hand.append(deck[0])
        deck.remove(deck[0])

    print(hand)
    print(len(deck))
    
deck = create_deck()
deal_hand(deck)