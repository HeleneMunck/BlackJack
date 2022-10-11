import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True # to control our while loop later on

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # append cards from the Card class to the empty deck list


    def __str__(self):
        deck_comp = " "
        for card in self.deck:
            deck_comp += "\n" + card.__str__()   # this print out string representation of each card

        return "The deck has: " +deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()   # take the deck in the Deck class, pop off a card item of that list and set that to single_card
        return single_card


class Hand: # represents both the dealer and the player

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # the card passed in will be from the DECK class Deck.deal
        self.cards.append(card) # the card has a rank. we can use that to put into the self.value
        self.value += values[card.rank]
        # track our aces
        if card.rank == "ACE":
            self.aces += 1

    def adjust_for_ace(self):
        # we check if self value is > 21. we initially have ace as an 11, but we dont want that if we have > 21.
        # so > 21 and i still have a 21, then change ace to 1 instead of 11. (we treat the aelf.ace as a boolean, not an int.
        while self.value > 21 and self.aces > 0:
            self.value -= 10 # take my value and subtrack 10 from it
            self.aces -= 1 # and take my ace and substract 1 from it


class Chips:

    def __init__(self, total = 100):  # it starts at 100
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:

        try: chips.bet = int(input(f"How many chips would you like to bet?. You have {chips.total}: "))

        except:
            print("Provide a number")
        else:
            if chips.bet > chips.total:
                print(f"Sorry you dont have enough chips. you have {chips.total}")
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):

    global playing   # this is used to control upcoming loop

    while True:
        x = input("Hit or Stand? Enter h or s: ")

        if x[0].lower() == "h":
            hit(deck, hand)

        elif x[0].lower() == "s":
            print("Player stands. Dealer's turn")
            playing = False

        else:
            print("Please enter h or s only")
            continue

        break


def show_some(player, dealer):
    # show only one of the dealers cards, but show all players cards
    print("\nDealer´s hand: ")
    print("First card hidden!")
    print(dealer.cards[1]) # shows only second item in dealers hand

    print("\nPlayers hand")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    # show all, and calcuate and display value. eg j+k == 20
    print("\nDealer's hand")
    for card in dealer.cards:
        print(card)
    print(f"Value of dealer's hand is: {dealer.value}")

    print("\nPlayers hand")
    for card in player.cards:
        print(card)
    print(f"Value of player's hand is: {player.value}")


def player_busts(player, dealer, chips):
    print("Bust Player!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player Wins! Dealer Bust!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins! Bust Player!")
    chips.lose_bet()


def push(player, dealer):
    print("dealer and player tie. Push")


# Game logic

while True:

    print("Welcome to BlackJack")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

# set up players chips

    player_chips = Chips()

    take_bet(player_chips)

# show some cards

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player.busts(player_hand, dealer_hand, player_chips)

            break

        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

        print(f"\nPlayer total chips are at: {player_chips.total}")

        new_game = input("Would you like to play again? y/n)")

        if new_game[0].lower() == "y":
            playing = True

            continue

        else:
            print("Thank you for playing!")

            break










###

# test a deck and shuffle it
#test_deck = Deck()
#test_deck.shuffle()

# Player
#test_player = Hand()
# deal one card from the deck CARD(suit, rank)
#pulled_card = test_deck.deal()
#print(pulled_card)
#test_player.add_card(pulled_card)
#print(test_player.value)

# test_player.add_card(test_deck.deal())
# test_player.value

####

