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





 #
 # MAIN GAME PLAY FUNCTIONS  
 # 

def player1_turn():
    print(f'\n\nYour turn. Here is your hand: {player_1.hand}. Choose a card value to' +
           ' request from your opponent. It must be a value in your hand\n')
    match_found = request_card(str(input('Enter your choice here and press ENTER: ')), player_1, computer)

    if match_found:
        print('You found a match. You get to go again!!')
        check_for_books()
        player1_turn()
    else:
        print('GO FISH!!')
        computer_turn()

    print(player_1)
    print(computer)

def computer_turn():
    print('It\'s the computer\'s turn now')
    index_requested = random.randint(0, len(computer.hand)-1)
    match_found = request_card(computer.hand[index_requested], computer, player_1)
    print(f'the index generated is {index_requested}, and the card is {computer.hand[index_requested]}')

    if match_found:
        print('You have the card the computer requested.')
        check_for_books()
        computer_turn()
    else:
        print('You don\'t have the card the computer requested. The computer is going fishing!')
        player1_turn()

    print(player_1)
    print(computer)

def request_card(card, requester, donator):
    match_found = False
    for c in donator.hand:
        if c == card:
            requester.hand.append(c)
            donator.hand.remove(c)
            match_found = True
    return match_found

    

def check_for_books():
    print('This method will check to see if a user has any new books.')


deck = create_deck()
deal_hand(deck)
player_1, computer = initialize_players()

player1_turn()