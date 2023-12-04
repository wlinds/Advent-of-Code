import os
import numpy as np

def puzzle_importer(file="2023/Python/data/puzzle_3.txt"):
    with open(file, 'r') as f:
        puzzle_string = f.read()
        lines = puzzle_string.split('\n')
        return [list(line.strip()) for line in lines], puzzle_string

puzzle_input, puzzle_string = puzzle_importer()

symbols = set()
for c in puzzle_string:
    if c == "." or c == "\n" or c.isdigit():
        pass
    else:
        symbols.add(c)

print(len(puzzle_input), len(puzzle_input[0]))

# 140 x 140 grid. Find adjacents.
# I'll try creating a 2D plane and check coordinates for matches??

# In hindsight this was a very bad decision since the numbers take up multiple coordinates

def fill_plane(puzzle_input):
    rows, cols = len(puzzle_input), len(puzzle_input[0])
    plane = np.empty((rows, cols), dtype='U1')

    for i in range(rows):
        for j in range(cols):
                plane[i, j] = puzzle_input[i][j]

    return plane

plane = fill_plane(puzzle_input)
print(plane.shape)
print((plane[1,-11]) == "*")

def get_symbol_pos(plane, symbols):
    rows, cols = plane.shape
    coordinates = {}

    for i in range(rows):
        for j in range(cols):
            char = plane[i, j]
            if char in symbols:
                if char not in coordinates:
                    coordinates[char] = []
                coordinates[char].append([i, j])

    return coordinates

def get_number_pos(plane):
    rows, cols = plane.shape
    adjacent_numbers = []

    for i in range(rows):
        current_number = ""
        current_number_start = -1
        coordinates = []

        for j in range(cols):
            if plane[i, j].isdigit():
                if current_number == "":
                    current_number_start = j  # start index for found number
                current_number += plane[i, j]
                coordinates.append([i, j])
            elif current_number:
                adjacent_numbers.append((int(current_number), current_number_start, coordinates.copy()))

                #reset
                current_number = ""
                current_number_start = -1
                coordinates = []

        if current_number:
            adjacent_numbers.append((int(current_number), current_number_start, coordinates.copy()))

    return adjacent_numbers



number_pos = get_number_pos(plane)
symbols_pos = get_symbol_pos(plane, symbols)


def find_adjacant(number_pos, symbols_pos):
    adjacent_pairs = []

    for number in number_pos:
        number_value, number_start, number_coordinates = number

        for symbol, symbol_coordinates_list in symbols_pos.items():
            for symbol_coordinates in symbol_coordinates_list:
                for number_coordinate in number_coordinates:

                    if (
                        abs(symbol_coordinates[0] - number_coordinate[0]) <= 1
                        and abs(symbol_coordinates[1] - number_coordinate[1]) <= 1
                    ):
                        adjacent_pairs.append((number_value, number_coordinates, symbol, symbol_coordinates))
                        break 

    return adjacent_pairs

adjacent_pairs = find_adjacant(number_pos, symbols_pos)
print(adjacent_pairs)

sum = 0
for i in adjacent_pairs:
    sum += int(i[0])

print(sum)

# Part 2

def find_adjacant_2(number_pos, symbols_pos, symbol='*'):
    adjacent_pairs = []

    for symbol_coordinates in symbols_pos.get(symbol, []):
        adjacent_numbers = []

        for number in number_pos:
            number_value, _, number_coordinates = number

            for number_coordinate in number_coordinates:

                if (
                    abs(symbol_coordinates[0] - number_coordinate[0]) <= 1
                    and abs(symbol_coordinates[1] - number_coordinate[1]) <= 1
                ):
                    adjacent_numbers.append(number_value)
                    break 

        if len(adjacent_numbers) == 2:
            adjacent_pairs.append((adjacent_numbers[0], adjacent_numbers[1], symbol_coordinates))

    return adjacent_pairs


adjacent_pairs = find_adjacant_2(number_pos, symbols_pos)


total_product = 0

for pair in adjacent_pairs:
    num1, num2, _ = pair
    product = num1 * num2
    total_product += product

print(total_product)
