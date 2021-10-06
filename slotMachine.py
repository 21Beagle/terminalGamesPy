import random

slot_values = ['A', 'K', 'Q', 'J', '10', '9', '8', '6', '5', '4', '3', '2']

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


for i in range(0, 3):
    result = get_line()
    results_board.append(result)
    print(results_board)
    print(result)
    result.clear()

print(results_board)