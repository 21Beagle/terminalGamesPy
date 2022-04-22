from cgi import test
from random import randint
from time import sleep

from termcolor import colored

from adjectives import adjectively, adjectives
from cities import cities
from items import items
from names import names
from verbs import verbs, verbspt
from hello import hello


def choose(array):
    if array == []:
        return None
    else:
        return array[randint(0, len(array) - 1)]


class Rarity:
    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        self.value = value


rarities = [
    Rarity("common", "white", 1),
    Rarity("uncommon", "green", 3),
    Rarity("rare", "magenta", 5),
    Rarity("legendary", "yellow", 10),
    Rarity("mythical", "red", 25),
    Rarity("artifact", "blue", 50),
    Rarity("godly", "cyan", 1000),
]


def choose_rarity():
    final_rarity = Rarity("common", "white", 1)
    for rarity in rarities:
        if randint(0, rarity.value) == 0:
            final_rarity = rarity
    return final_rarity


class Item:
    def __init__(self):
        self._rarity = choose_rarity()
        self.rarity = colored(self._rarity.name, self._rarity.color)

        self._value = (
            randint(1, 5) * self._rarity.value + randint(1, 20) + self._rarity.value
        )

        self.value = colored(str(self._value), "yellow", attrs=["bold"])

        self.noun = choose(items)
        self.adjective = choose(adjectives)
        self._name = self.adjective + " " + self.noun
        self.name = colored(self._name.title(), self._rarity.color, attrs=["bold"])

    def description(self):
        return (
            self.name + " is a " + self.rarity + " item worth " + self.value + " gold."
        )


def generate_items(number):
    item_list = []
    for i in range(number):
        item_list.append(Item())
    return item_list


class Backpack:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        return self.items.remove(item)

    def print_contents(self):
        index = 0
        for item in self.items:
            print(str(index) + ". " + item.description())
            index += 1


class Player:
    def __init__(self, name=choose(names), money=0):
        self._name = name
        self.name = colored(self._name, "green", attrs=["bold", "underline"])
        self.backpack = Backpack()
        self.items = self.backpack.items
        self._money = int(money)
        self.money = colored(money, "yellow", attrs=["bold"])

    def sell(self, item):
        amount = self.backpack.remove(item)
        self._money += amount
        self.money = colored(self._money, "yellow", attrs=["bold"])
        print(self.name, "sold", item.name, "for", item.value, "gold.")
        print(self.name + " now has " + self.money + " gold.")

    def talk(self, message):
        print(self.name + ": " + message)


class NPC:
    def __init__(self, money):
        self.adjective = choose(adjectives)
        self.verbpt = choose(verbspt)
        self._first_name = choose(names)
        self._last_name = choose(names)
        self._name = (
            self._first_name + " " + self._last_name + ", the " + self.adjective
        )
        self.name = colored(self._name.title(), "blue")
        self.backpack = Backpack()
        self._money = int(money)
        self.money = colored(money, "yellow", attrs=["bold"])

    def introduce(self):
        print(choose(hello) + ", I am " + self.name + ".")

    def shop(self):
        if len(self.backpack.items) == 0:
            print(self.name + ": I have nothing to sell.")
        else:
            print(self.name + ": I have the following items for sale:")
            print("")
            self.backpack.print_contents()
            print("")
            print(self.name + ": How may I help you?")

    def add_item(self, item):
        self.backpack.add(item)


class City:
    def __init__(self, options=[]):
        self._name = choose(cities)
        self.name = colored(self._name.title(), "yellow", attrs=["bold"])
        self.options = options
        self.NPCS = [NPC(randint(1, 100)) for i in range(randint(1, 5))]


def travel_text(player_name, city_name, winning_item_name):

    travel_text = ""
    travel_text += player_name + " "
    travel_text += choose(adjectively)
    travel_text += " " + choose(verbspt)
    travel_text += " to "
    travel_text += city_name
    travel_text += " in search of a "
    travel_text += winning_item_name + "."
    print(travel_text)


def time_passes():
    sleep(2)
    print(".")
    sleep(0.5)
    print("..")
    sleep(0.5)
    print("...")
    sleep(1)


def options_text(options):
    index = 0
    for option in options:
        print(str(index) + ". " + option.text)
        index += 1


def choose_option(options):
    option_number = input("Choose an option: ")
    option_number = int(option_number)
    return options[option_number].action


def quest_text(player):
    pass


def choose_with_removal(array):
    item = choose(array)
    array.remove(item)
    return item


def generate_cities(number):
    cities = []
    for i in range(number):
        cities.append(City())
    return cities


possible_items = generate_items(50)
winning_item = possible_items[0]
prize_item = choose_with_removal(possible_items)
cities_list = generate_cities(randint(4, 8))

while possible_items != []:
    city = choose(cities_list)
    npc = choose(city.NPCS)
    item = choose_with_removal(possible_items)
    npc.add_item(item)

for city in cities_list:
    for npc in city.NPCS:
        npc.introduce()
        npc.shop()


def intro():

    print("Welcome to the game!")
    name = input("What is your name? ")
    player = Player(name, 100)

    sleep(2)
    print("Hello", player.name + ", odd name you have there.")

    item_guy = NPC(0)

    time_passes()
    print("Then we shall begin.")
    time_passes()

    print(player.name + " wakes up in a smokey room.")
    print("It is dark and cold.")
    print("A figure approaches " + player.name + ".")
    print("My name is " + item_guy.name + ".")
    print("I need an", winning_item.name, "for a collection.")
    print("I will give you a", prize_item.name, "if you can find me one.")
    print("Please find me a " + winning_item.name + ".")
    print("You will be rewarded...")

    time_passes()


def game():
    pass


intro()
