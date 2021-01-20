import random
import collections
import sys
import time

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


# There will be two players in this game. The user, and the computer
class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.books = 0

    def __str__(self):
        return f'Name: {self.name}\t\tBooks: {self.books}'


# This function creates a shuffled deck with 52 cards
def create_deck():
    deck = cards * 4
    random.shuffle(deck)
    return deck


# This function creates objects for each of the players
def initialize_players():
    human = Player('Human', deal_hand(deck))
    computer = Player('Computer', deal_hand(deck))
    return human, computer


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

def human_turn():
    print('\n\n------------TURN: Human------------\n')
    print(human)
    print(f'{computer}\n')
    if len(human.hand) > 0:
        print(f'Your turn. Here is your hand: {human.hand}. Choose a card value to' +
            ' request from your opponent. It must be a value in your hand\n')

        match_found = request_card(get_user_input(), human, computer)

        if match_found:
            print('You found a match. You get to go again!!')
            check_for_books(human)
            pause_between_turns()
            human_turn()
        else:
            go_fish(human)
            print(f'\nGO FISH! The card that was chosen from the deck is {human.hand[-1]}')
            check_for_books(human)
            pause_between_turns()
            computer_turn()
    elif out_of_cards(human, computer):
        pause_between_turns()
        computer_turn()


def computer_turn():
    print('\n------------TURN: Computer------------\n')
    print(human)
    print(f'{computer}\n')
    if len(computer.hand) > 0:
        print('It\'s the computer\'s turn now')
        index_requested = random.randint(0, len(computer.hand) - 1)
        print(f'The computer requested a {computer.hand[index_requested]}')
        match_found = request_card(computer.hand[index_requested], computer, human)

        if match_found:
            print('You HAVE the card the computer requested.')
            check_for_books(computer)
            time.sleep(3)
            computer_turn()
        else:
            print('You DO NOT have the card the computer requested. The computer is going fishing!')
            go_fish(computer)
            check_for_books(computer)
            pause_between_turns()
            human_turn()
    elif out_of_cards(computer, human):
        pause_between_turns()
        human_turn()
    


def out_of_cards(player, opponent):
    if go_fish(player):
        if request_card(player.hand[0], player, opponent):
            print(f'{opponent.name} has the card that {player.name} requested!')
        else:
            print(f'{opponent} does not have the card that {player.name} requested. It\'s {opponent.name}\'s turn now.')
        print(human)
        return True        
    else:
        check_for_books(player)
        check_for_books(opponent)
        determine_results()


def pause_between_turns():
    time.sleep(1)


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
        player.hand.append(deck[0])
        deck.remove(deck[0])
        return True
    else:
        print('The deck is empty. Once you run out of cards in your hand, the game will be over.')
        return False


def get_user_input():
    user_input = str(input('Please enter your selection here, and press ENTER: '))
    while user_input.upper() not in human.hand:
        user_input = str(input('\nYour selection must be a card value in your hand. Please enter your selection here, and press ENTER: '))
    return user_input


def check_for_books(player):
    counter = collections.Counter(player.hand)

    for key in counter:
        if counter[key] == 4:
            player.books += 1
            while key in player.hand:
                player.hand.remove(key)
            print(f'{player.name} made a book of {key}\'s')
            print(human)
            print(computer)
            


def determine_results():
    print('The game is over. There are no more cards in the deck.\n')
    if computer.books > human.books:
        print('The COMPUTER won...\n')
    elif computer.books == human.books:
        print('It was a tie...\n')
    else:
        print('YOU WON!!!\n')
    print(f'Your books: {human.books}\nComputer books: {computer.books}')
    sys.exit()


deck = create_deck()
human, computer = initialize_players()
human_turn()