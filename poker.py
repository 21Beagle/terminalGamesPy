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
                value = i + 2
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

    def return_card(self, player, card):
        self.cards.append(player.return_card(card))


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        hand_length = len(self.hand)
        hand_str = ""
        for i in range(hand_length):
            hand_str +=self.hand[i].face + " "
        print(hand_str)

    def return_card(self, index):
        return self.hand.pop(index)  

    def value_hand(self):
        return hand_value(self.hand) 


def duplicates_check(hand):
    last_card = len(hand)
    pairs = []
    for i in range(last_card):
        for j in range(i+1, last_card):
            if hand[i].value == hand[j].value:
                pairs.append([hand[i].face, hand[j].face])

    how_many = len(pairs)
    return how_many

def pairs_value(hand):
    duplicates = duplicates_check(hand)
    if duplicates == 1:
        return "Pair"
    if duplicates == 2:
        return "Two pair"
    if duplicates == 3:
        return "Three of a kind"
    if duplicates == 4:
        return "Full house"
    if duplicates == 6:
        return "Four of a kind"
    else:
        return "High Card"


def high_card_check(hand):
    last_card = len(hand)
    cards_values = []
    for i in range(last_card):
        cards_values.append(hand[i].value)
    highest_value = max(cards_values) - 2
    return card_values[highest_value]




def straight_check(hand):
    last_card = len(hand)
    hand_values_a1 = []
    hand_values_a13 = []
    straight_a1 = []
    straight_a13 = []
    for i in range(last_card):
        if hand[i].value == 14:
            hand_values_a13.append(14)
            hand_values_a1.append(1)
        else:
            hand_values_a13.append(hand[i].value)
            hand_values_a1.append(hand[i].value)
    hand_values_a1.sort()
    hand_values_a13.sort()
    for i in range(last_card-1):
        if hand_values_a1[i] + 1 != hand_values_a1[i+1] :
            straight_a1.append(False)
        else:
            straight_a1.append(True)
        if hand_values_a13[i] + 1 != hand_values_a13[i+1] :
            straight_a13.append(False)
        else:
            straight_a13.append(True)
    if all(straight_a1) or all(straight_a13):
        return True
    else:
        return False


def flush_check(hand):
    last_card = len(hand)
    for i in range(last_card - 1):
        if hand[i].suit != hand[i+1].suit:
            return False
    return True

def hand_value(hand):
    high_card = high_card_check(hand)
    straight = straight_check(hand)
    flush = flush_check(hand)
    if flush and straight and high_card == "A":
        return "Royal Flush"
    if flush and straight:
        return "Straight Flush"
    if flush == True:
        return "Flush"
    if straight == True:
        return "Straight"
    return pairs_value(hand)
    



deck = Deck()
deck.shuffle()

jack = Player("Jack")


money = 100
while money > 0:

    print("Money:", money)

    bet = input("how much to bet?")
    for i in range(5):
        jack.draw(deck) 
    jack.show_hand()

    swap_str = input("what cards to swap?")
    number_swap = len(swap_str)
    list_swap = []
    for i in range(number_swap):
        number = swap_str[i]
        number = int(number)
        list_swap.append(number)

    list_swap.sort()

    for i in range(number_swap - 1, -1, -1):
        jack.return_card(list_swap[i])
        jack.draw(deck)

    jack.show_hand()
    print(jack.value_hand())

    for i in range(5):
        jack.return_card(0)

for j in range(10000000):
    deck.shuffle()

    jack_hand = ""
   










time.sleep(10000)

