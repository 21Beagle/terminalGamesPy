import random
import time
from termcolor import colored

colours = ['red', 'yellow', 'blue', 'green']

card_values = "23456789TJQKA"

def suit(colour):
    if colour == 'red':
        return 'Hearts'
    if colour == 'yellow':
        return 'Spades'
    if colour == 'blue':
        return 'Diamonds'
    if colour == 'green':
        return 'Clubs'


class Card(object):
    def __init__(self, face, value, colour):
        self.face = colored(face, colour)
        self.value = value
        self.suit = suit(colour)

    def show(self):
        return self.face


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for colour in colours:
            for i in range(0, len(card_values)):
                face = card_values[i]
                value = i + 1
                self.cards.append(Card(face, value, colour))
    
    def show(self):
        for card in self.cards:
            card.show()
            return card.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0 , -1):
            rand_num = random.randint(0, i)
            self.cards[i], self.cards[rand_num] = self.cards[rand_num], self.cards [i]
    
    def draw_card(self):
        return self.cards.pop()

    def return_card(self, player):
        self.cards.append(player.return_card())




class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

    def return_card(self):
        return self.hand.pop()   

def pair_check(hand):
    last_card = len(hand)
    pairs = []
    for i in range(last_card):
        for j in range(i+1, last_card):
            if hand[i].value == hand[j].value:
                pairs.append([hand[i].face, hand[j].face])

    how_many = len(pairs)
    print(how_many)
    return how_many
    





deck = Deck()
deck.shuffle()

jack = Player("Jack")
bob = Player("Bob")

for j in range(10000):
    deck.shuffle()

    jack_hand = ""
    bob_hand = ""
    for i in range(5):
        jack.draw(deck)
        bob.draw(deck)
    for i in range(5):
        jack_hand+=jack.hand[i].face + " "
        bob_hand+=bob.hand[i].face + " "  
    print(jack_hand)
    pair_check(jack.hand)
    print(bob_hand)
    pair_check(bob.hand)
    for i in range(5):
        deck.return_card(jack)
        deck.return_card(bob)








time.sleep(10000)

