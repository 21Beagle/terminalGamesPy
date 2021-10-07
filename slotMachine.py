import random
import os
import time
import os

import os
def clear(): os.system('cls') #on Windows System
clear()


slot_values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '6', '5', '4', '3', '2']

slot_values_length = len(slot_values)
slot_values_weighted = []


for i in range(slot_values_length):
    slot_value = slot_values[i]
    for j in range(1, i+2):
        slot_values_weighted.append(slot_value)

slot_values_weighted_length = len(slot_values_weighted)

slot_values = slot_values_weighted
slot_values_length = slot_values_weighted_length


results_board = []

def get_line(number_of_columns = 5, slot_values = slot_values):
    result = []
    slot_values_length = len(slot_values)
    for i in range(0, number_of_columns):
        index = random.randint(0, slot_values_length-1)
        result.append(slot_values[index])
    return result

def get_new_board(rows = 3, columns = 5):
    results_board.clear()
    for i in range(0, rows):
        results = get_line(columns)
        results_board.append(results)
    return results_board

def print_machine(results_board = []):
    machine = ""
    surround = (2 * len(results_board[0]) - 1) * "=" + "\n"
    machine += surround

    for i in results_board:
        index = results_board.index(i)
        for j in results_board[index]:
            jndex = results_board[index].index(j)
            machine += results_board[index][jndex]
            machine += " "
        machine += "\n"
    machine += surround
    print(machine)
    return machine

def get_board_and_print(time_length):
    results_board = get_new_board()
    print_machine(results_board)
    time.sleep(time_length)


i = 0.05
for j in range(0, 14):
    get_board_and_print(i)
    clear()
    i += j * 0.01
get_board_and_print(i)
print("Unlucky!")

time.sleep(10)