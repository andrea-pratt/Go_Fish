import random
import collections
import sys

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []

# There will be two players in this game. The user, and the computer
class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.books = 0

    def __str__(self):
        return f'Name: {self.name} Hand: {self.hand} Books: {self.books}'

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

    if len(computer.hand) > 0:
        match_found = request_card(str(input('Enter your choice here and press ENETER: ')), player_1, computer)
    else:
        if not go_fish(player_1):
            determine_results()

    if match_found:
        print('You found a match. You get to go again!!')
        check_for_books(player_1)
        print(computer)
        player1_turn()
    else:
        print('GO FISH!!')
        go_fish(player_1)
        check_for_books(player_1)
        print(player_1)
        print(computer)
        computer_turn()


def computer_turn():
    print('It\'s the computer\'s turn now')
    index_requested = random.randint(0, len(computer.hand)-1)
    if len(player_1.hand) > 0:
        match_found = request_card(computer.hand[index_requested], computer, player_1)
    else:
        if not go_fish(computer):
            determine_results()
    if match_found:
        print('You have the card the computer requested.')
        check_for_books(computer)
        computer_turn()
    else:
        print('You don\'t have the card the computer requested. The computer is going fishing!')
        go_fish(computer)
        check_for_books(computer)
        print(player_1)
        print(computer)
        player1_turn()

    

def request_card(card, requester, donator):
    match_found = False
    if len(donator.hand) > 0:
        while card in donator.hand:
            donator.hand.remove(card)
            requester.hand.append(card)
            match_found = True
    return match_found


def go_fish(player):
     if len(deck) > 0:
        print(f'The card that was chosen from the deck is {deck[0]}')
        player.hand.append(deck[0])
        deck.remove(deck[0])
        return True
     else:
         print('The deck is empty. Once you run out of cards in your hand, the game will be over.')
         return False


def check_for_books(player):
    print('This method will check to see if a user has any new books.')  
    counter = collections.Counter(player.hand)

    for key in counter:
        if counter[key] == 4:
            player.books += 1
            while key in player.hand:
                player.hand.remove(key)
            print(f'{player.name} made a book of {key}\'s')
            print(player_1)
            print(computer)


def determine_results():
    print('The game is over. There are no more cards in the deck.\n')
    if computer.books > player_1.books:
        print('The COMPUTER won...\n')
    elif computer.books == player_1.books:
        print('It was a tie...\n')
    else:
        print('YOU WON!!!\n')
    print(f'Your books: {player_1.books}\nComputer books: {computer.books}')
    sys.exit()
    

deck = create_deck()
deal_hand(deck)
player_1, computer = initialize_players()

player1_turn()