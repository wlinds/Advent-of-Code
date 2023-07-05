import csv
import numpy as np

# INTCODE 
opcodes = [1, 2, 99]

# Opcode 1 adds together numbers
# Opcode 2 multiplies the two inputs
# Opcode 99 means that the program is finished and should immediately halt

with open("2019/day2.txt", "r") as file:
    list = [int(i) for i in file.read().split(",")]


def int_comp(list):
    for i in range(0, len(list), 4):
        x, y, cursor = list[list[i+1]], list[list[i+2]], list[i+3]

        if list[i] == 99:
            print('Finished')
            print(list[0])
            return list[0]
        elif list[i] == 1:
            list[cursor] = x + y
        elif list[i] == 2:
            list[cursor] = x * y

def twelve_o_two_program_alarm(list):
    list[1] = 12
    list[2] = 2
    return int_comp(list)

def int_comp(data):
    for i in range(0, len(data), 4):
        print(i)
        x, y, cursor = data[data[i+1]], data[data[i+2]], data[i+3]

        if data[i] == 99:
            print('Finished')
            print(data[0])
            return data[0]
        elif data[i] == 1:
            data[cursor] = x + y
        elif data[i] == 2:
            data[cursor] = x * y



# determine what pair of inputs produces the output 19690720

# 100 * noun + verb

noun = 12
verb = 2
ans = 1202

import numpy as np

def int_comp2(data):

    data[1] = np.random.randint(0,99)
    data[2] = np.random.randint(0,99)

    for i in range(0, len(data), 4):
        x, y, cursor = data[data[i+1]], data[data[i+2]], data[i+3]

        if data[i] == 99:
            print('Finished')
            print(data[0])
            print(data[1], data[2])
            return data[0], data[1], data[2]
        elif data[i] == 1:
            data[cursor] = x + y
        elif data[i] == 2:
            data[cursor] = x * y

if __name__ == "__main__":
    print(list)

    while int_comp2(data=list.copy())[0] != 19690720:
        print("loop")
        int_comp2(data=list.copy())