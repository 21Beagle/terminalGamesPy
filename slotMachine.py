import random
import os
import time
import os
from termcolor import colored

import os
def clear(): os.system('cls') #on Windows System
clear()


slot_values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '6', '5', '4', '3', '2']
colours = ['red', 'yellow', 'blue', 'green']

slot_values_length = len(slot_values)
slot_values_weighted = []



for i in range(slot_values_length):
    slot_value = slot_values[i]
    for colour in colours:
        for j in range(1, i+2):
            slot_values_weighted.append(colored(slot_value, colour))

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

def get_new_board(rows = 60, columns = 5):
    results_board.clear()
    for i in range(0, rows):
        results = get_line(columns)
        results_board.append(results)
    return results_board

big_board = get_new_board()
big_rows = len(big_board)
big_columns = len(big_board[big_rows-1])

def get_row(row_number, big_board = big_board):
    big_rows = len(big_board)
    big_columns = len(big_board[big_rows-1])
    output_string = " ╔═══╦═══╦═══╦═══╦═══╗\n"
#1
    output_string += " ║ "
    for j in range(big_columns):
        if j % 2 == 0:
            y = row_number - 2
            x = j
            output_string += big_board[y][x] + " ║ "

        if j % 2 != 0:
            y = big_rows - row_number - 4
            x = j 
            output_string += big_board[y][x]  + " ║ "
    
    output_string += "\n ║ "
#2
    for j in range(big_columns):
        if j % 2 == 0:
            y = row_number - 1
            x = j
            output_string += big_board[y][x] + " ║ "
        if j % 2 != 0:
            y = big_rows - row_number - 3
            x = j 
            output_string += big_board[y][x]  + " ║ "
    output_string += "\n ║ "
#3
    for j in range(big_columns):
        if j % 2 == 0:
            y = row_number
            x = j
            output_string += big_board[y][x] + " ║ "
        if j % 2 != 0:
            y = big_rows - row_number - 2
            x = j 
            output_string += big_board[y][x]  + " ║ "

    
    output_string += "\n ║ "
#4
    for j in range(big_columns):
        if j % 2 == 0:
            y = row_number + 1
            x = j
            output_string += big_board[y][x] + " ║ "
        if j % 2 != 0:
            y = big_rows - row_number - 1
            x = j
            output_string += big_board[y][x]  + " ║ "
    output_string += "\n ║ "
#5
    for j in range(big_columns):
        if j % 2 == 0:
            y = row_number + 2
            x = j
            output_string += big_board[y][x] + " ║ "
        if j % 2 != 0:
            y = big_rows - row_number 
            x = j
            output_string += big_board[y][x]  + " ║ "
    output_string += "\n ╚═══╩═══╩═══╩═══╩═══╝"

    return output_string


def spin():
    timer = 0.05
    for i in range(3, 30):
        board = get_row(i-1)
        print(board)
        time.sleep(timer)
        clear()

    for i in range(30, 46):
        board = get_row(i-1)
        print(board)
        time.sleep(timer)
        timer += 0.03
        if i < 45:
            clear()
        else:
            time.sleep(2)
            final_board = get_row(44)
            print("       !You won!")
            break

    print(final_board)


spin()
time.sleep(10)

