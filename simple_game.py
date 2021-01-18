import random 
import dataclasses

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []

# There will be two players in this game. The user, and the computer
class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return f'Name: {self.name} Hand: {self.hand}'



# This function creates a shuffled deck with 52 cards
def create_deck():
    deck = cards*4
    random.shuffle(deck)
    return deck


# This function creates objects for each of the players
def initialize_players():
    player_1 = Player('Player_1', deal_hand(deck))
    computer = Player('Computer', deal_hand(deck))
    print(player_1)
    print(computer)
    return player_1, computer
    

# This function creates a hand with 7 cards from the top of the deck
def deal_hand(deck):
    hand = []
    for _ in range(7):
        hand.append(deck[0])
        deck.remove(deck[0])
    return hand


deck = create_deck()
deal_hand(deck)
player_1, computer = initialize_players()


 #
 # MAIN GAME PLAY FUNCTIONS  
 # 

def player1_turn():
    print(f'Your turn. Here is your hand: {player_1.hand}. Choose a card value to' +
           ' request from your opponent. It must be a card value in your hand')

player1_turn()