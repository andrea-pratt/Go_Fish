import random
import collections
import sys
import time

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []


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

# Calls game setup functions and starts the application
def Main():
    # Will catch general exceptions
    try:
        print('\n\n\nREADY TO PLAY THE GAME OF GO FISH? LET\'S GET STARTED!')
        human_turn()
    except:
        print('I\'m sorry. Something went wrong. Please exit the game and start again')

# This block of code runs whenever it's the user's turn in the game
# It checks to see if the user has cards in there hand, and if so,
# allows them to request one of the values in their hand from the computer.
# If the computer has the requested card value, they must give all cards
# of that value to the user, and the user gets another turn.
# If the computer hand doesn't contain the requested card value, the user
# will draw a card from the deck
def human_turn():
    # Print current turn and game stats
    print('\n------------TURN: Human------------\n') 
    print(human)                    
    print(f'{computer}\n')
    # Make sure user has cards in their hand
    if len(human.hand) > 0:
        print(f'Your turn. Here is your hand: {human.hand}. Choose a card value to' +
            ' request from your opponent. It must be a value in your hand\n')
        # Request a card from the computer using user input. Saves the bool
        # return value in a variable for later use
        match_found = request_card(get_user_input(), human, computer)
        # If the requested card is in the computer's hand, check to see if the user made any books (4 cards of the same value),
        # pause to allow the user to read print statements, and start their turn again
        if match_found:
            print('You found a match. You get to go again!!')
            check_for_books(human)
            pause_between_turns()
            human_turn()
        # If the computer doesn't have the requested card, call the go_fish method to draw a card from the deck,
        # display the card drawn, check for books, wait 3 seconds, and then go to the computer's turn
        else:
            go_fish(human)
            print(f'\nGO FISH! The card that was chosen from the deck is {human.hand[-1]}')
            check_for_books(human)
            pause_between_turns()
            computer_turn()
    # If the computer runs out of cards, they get to draw one card from the deck and see if their opponent has that card value
    # if not, their turn is over. If the deck is empty, the game ends.
    elif out_of_cards(human, computer):
        pause_between_turns()
        computer_turn()

# This function runs whenever it's the computer's turn in the game.
# Funtionality is nearly the same as the player turn
def computer_turn():
    print('\n------------TURN: Computer------------\n')
    print(human)
    print(f'{computer}\n')
    if len(computer.hand) > 0:
        print('It\'s the computer\'s turn now')
        # Requests a card from the user based on a randomly generated index of it's hand
        index_requested = random.randint(0, len(computer.hand) - 1)
        print(f'The computer requested a(n) {computer.hand[index_requested]}')
        match_found = request_card(computer.hand[index_requested], computer, human)

        if match_found:
            print('You HAVE the card the computer requested.')
            check_for_books(computer)
            pause_between_turns()
            computer_turn()
        else:
            print('You DO NOT have the card the computer requested. The computer is going fishing!')
            go_fish(computer)
            check_for_books(computer)
            pause_between_turns()
            human_turn()
    elif out_of_cards(computer, human):
        print('You ran out of cards in your hand...')
        pause_between_turns()
        human_turn()
    

# If either player runs out of cards in their hand, this method is called
def out_of_cards(player, opponent):
    # Attempts to draw a card from the deck and requests that cards value from the other player
    # If the opponent has the card request, the player gets to go again, otherwise their turn is over
    if go_fish(player):
        if request_card(player.hand[0], player, opponent):
            print(f'{opponent.name} has the card that {player.name} requested!')
        else:
            print(f'{opponent} does not have the card that {player.name} requested. It\'s {opponent.name}\'s turn now.')
        check_for_books(player)
        return True     
    # If the deck is empty, check for books for both players and determine the game results   
    else:
        check_for_books(player)
        check_for_books(opponent)
        determine_results()

# This function allows time for the user to read print statements during the game
def pause_between_turns():
    time.sleep(3)

# This function determine whether or not the requested card is in the
# other player's hand. If there's a match, it transfers all cards of that
# value to the requester's hand, and returns True
def request_card(card, requester, donator):
    match_found = False
    if len(donator.hand) > 0:
        while card in donator.hand:
            donator.hand.remove(card)
            requester.hand.append(card)
            match_found = True
    return match_found

# Attempts to transfer one card from the deck, to the players hand.
# If the deck is empty, it will print a message and return False
def go_fish(player):
    if len(deck) > 0:
        player.hand.append(deck[0])
        deck.remove(deck[0])
        return True
    else:
        print('The deck is empty. Once you run out of cards in your hand, the game will be over.')
        return False

# Provides a method to get the user's card selection and provides data validation to ensure selected card is in their hand
def get_user_input():
    user_input = str(input('Please enter your selection here, and press ENTER: '))
    while user_input.upper() not in human.hand:
        user_input = str(input('\nYour selection must be a card value in your hand. Please enter your selection here, and press ENTER: '))
    return user_input

# This function determines the frequency of all values in a given player's hand. 
# If it finds a value with a frequency of 4, it removes those cards from their hand
# and adds 1 to the player's books
def check_for_books(player):
    counter = collections.Counter(player.hand)

    for key in counter:
        if counter[key] == 4:
            player.books += 1
            while key in player.hand:
                player.hand.remove(key)
            # When a player gets a new book, it displays this message and the current game stats
            print(f'{player.name} made a book of {key}\'s')
            print(human)
            print(computer)
            

# This function tests to see which player has more books at the end of the game
# and prints appropriate messages. It then exits the application
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


# Call setup functions and begin game play
deck = create_deck()
human, computer = initialize_players()
Main()
