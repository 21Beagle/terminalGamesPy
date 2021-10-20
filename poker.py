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
        print(self.face)
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





deck = Deck()
deck.shuffle()

jack = Player("Jack")
bob = Player("Bob")

for i in range(5):
    jack.draw(deck)
    bob.draw(deck)

jack.show_hand()
print("")
bob.show_hand()


