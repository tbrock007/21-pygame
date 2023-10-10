'''
Project: Twenty One Game:
Course: cs 1410-001
Name: Brock Terry
Due Date: Jan 22. 2023

Description:
For this project you will implement a game of 
Twenty-One with a dealer and one player using classes and 
objects to create the game. 


This is skeleton starter code for the Twenty-One Game.

Typical pseudocode for such a game would be:
1. initial deal
2. player's turn 
3. If player gets twenty-one, immediate win 
4. dealer's turn 
5. check for winner
6. print results
'''

import os
import random

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
numeric_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.numeric_value = numeric_values[value]
    
    def __str__(self):
        card_template = (
        f'┌───────┐\n'
        f'│{self.value:<2}     │\n'
        f'│       │\n'
        f'│   {suits_values[self.suit]}   │\n'
        f'│     {self.value:>2}│\n'
        f'└───────┘\n'
        )
        return card_template

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for suit in suits for value in cards]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.hand = []
        self.score = 0

    def hit(self, card):
        self.hand.append(card)
        self.score += card.numeric_value
        if self.score > 21:
            return "bust"

class Player(Hand):
    def __init__(self,deck):
        super().__init__()
        self.name = "Player"
        self.hit(deck.deal())
        self.hit(deck.deal())
    def stand(self):
        pass

class Dealer(Hand):
    def __init__(self,deck):
        super().__init__()
        self.name = "Dealer"
        self.hidden_card = None
        self.hit(deck.deal())
        self.hit(deck.deal())
    def hit(self, card):
        if not self.hidden_card:
            self.hidden_card = card
            return
        else:
            return super().hit(card)

    def reveal_hidden_card(self):
        self.hidden_card = self.hand.pop(0)
    
    def stand(self,deck):
        while self.score < 17:
            self.hit(deck.deal())

def clear():
    """Clear the console."""
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux, where os.name is 'posix'
    else:
        _ = os.system('clear')

def play_game():
    deck = Deck()
    deck.shuffle()

    player = Player(deck)
    dealer = Dealer(deck)

    clear()
    print(player.hand[0])
    print(player.hand[1])
    print("Player's score:", player.score)
    print()
    print(dealer.hand[0])
    print("Dealer's hidden card")
    print()

    dealer.reveal_hidden_card()
    dealer.stand(deck)
    dealer.score = sum(card.numeric_value for card in dealer.hand)
    
    #for card in dealer.hand:
        #print(card)
      #print("Dealer's score:", dealer.score)

    while True:
        player_choice = input("Do you want to hit or stand? ").lower()
        if player_choice == "hit":
            card = deck.deal()
            player.hit(card)
            clear()
            print("Player's hand:")
            for card in player.hand:
                print(card)
            print("Player's score:", player.score)
            print()
            print("Dealer's hand:")
            print(dealer.hand[0])
            print("Dealer's hidden card")
            print()
            if player.score > 21:
                print("Player busts. Dealer wins.")
                return
        elif player_choice == "stand":
            break
    dealer.stand(deck)
    print("Player's final hand:")
    for card in player.hand:
        print(card)
    print("Player's final score:", player.score)
    print()
    print("Dealer's final hand:")
    for card in dealer.hand:
        print(card)
    print("Dealer's final score:", dealer.score)
    print()
    if player.score == 21:
       print("BlackJack! Player wins!")
    elif player.score > dealer.score:
        print("Player wins!")
    elif dealer.score > 21:
        print("Dealer busts, Player wins!")
    elif dealer.score > player.score:
        print("Dealer wins.")
    else:
        print("It's a tie.")
            


play_game()





