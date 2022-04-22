from time import sleep
from random import randint
from items import items
from names import names
from cities import cities
from adjectives import adjectives, adjectively
from verbs import verbs, verbspt
from termcolor import colored


def choose(array):
    if array == []:
        return None
    else:
        return array[randint(0, len(array)-1)]


class Rarity:
    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        self.value = value


rarities = [Rarity("common", "white", 1),
            Rarity("uncommon", "green", 3),
            Rarity("rare", "magenta", 5),
            Rarity("legendary", "yellow", 10),
            Rarity("mythical", "red", 25),
            Rarity("artifact", "blue", 50),
            Rarity("godly", "cyan", 1000)]


def choose_rarity():
    final_rarity = Rarity("common", "white", 1)
    for rarity in rarities:
        if randint(0, rarity.value) == 0:
            final_rarity = rarity
    return final_rarity


class Item:
    def __init__(self):
        self._rarity = choose_rarity()
        self.rarity = colored(
            self._rarity.name, self._rarity.color)

        self._value = randint(1, 5) * self._rarity.value + \
            randint(1, 20) + self._rarity.value

        self.value = colored(str(self._value), "yellow", attrs=['bold'])

        self.noun = choose(items)
        self.adjective = choose(adjectives)
        self._name = self.adjective + " " + self.noun
        self.name = colored(self._name.title(),
                            self._rarity.color, attrs=['bold'])

    def description(self):
        return (self.name + " is a " + self.rarity + " item worth " + self.value + " gold.")


def generate_items(number):
    item_list = []
    for i in range(number):
        item_list.append(Item())
    return item_list


class Backpack:
    def __init__(self, items=[]):
        self.items = items

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
    def __init__(self, name, money):
        self._name = name
        self.name = colored(self._name, "green", attrs=['bold', "underline"])
        self.backpack = Backpack()
        self.items = self.backpack.items
        self._money = int(money)
        self.money = colored(money, "yellow", attrs=['bold'])

    def sell(self, item):
        amount = self.backpack.remove(item)
        self._money += amount
        self.money = colored(self._money, "yellow", attrs=['bold'])
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
        self._name = self._first_name + " " + self._last_name + ", the " + self.adjective
        self.name = colored(self._name.title(), "blue")
        self.backpack = Backpack()
        self._money = int(money)
        self.money = colored(money, "yellow", attrs=['bold'])


class option:
    def __init__(self, text, action):
        self.text = text
        self.action = action


def travel_text(player_name, winning_item_name):
    city = choose(cities)
    city = colored(city, "yellow")
    travel_text = ""
    travel_text += player_name + " "
    travel_text += choose(adjectively)
    travel_text += " " + choose(verbspt)
    travel_text += " to "
    travel_text += city
    travel_text += " in search of a "
    travel_text += winning_item_name + "."
    print(travel_text)

    return city


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


def game():
    print("Welcome to the game!")
    name = input("What is your name? ")
    player = Player(name, 100)

    sleep(2)
    print("Hello", player.name + ", odd name you have there.")

    possible_items = generate_items(50)
    winning_item = possible_items[0]

    item_guy = NPC(0)

    time_passes()
    print("Then we shall begin.")
    time_passes()

    print(player.name + " wakes up in a smokey room.")
    print("It is dark and cold.")
    print("A figure approaches " + player.name + ".")
    print("My name is " + item_guy.name + ".")
    print("I need an", winning_item.name, "for a collection, I am making.")
    print("Please find me a " + winning_item.name + ".")
    print("You will be rewarded...")

    time_passes()

    current_city = travel_text(player.name, winning_item.name)
    sleep(2)
    print(player.name + " has arrived at " + current_city + ".")


game()
