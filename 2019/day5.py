
# Opcode 1 adds together numbers
# Opcode 2 multiplies the two inputs
# Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.
# Opcode 4 outputs the value of its only parameter.
# Opcode 99 means that the program is finished and should immediately halt

# Opcode 5 jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
# Opcode 6 jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
# Opcode 7 less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
# Opcode 8 equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.

with open("2019/day5b.txt", "r") as file:
    puzzle_input = [int(i) for i in file.read().split(",")]

def parameter_mode(puzzle_input, instruction: int, i:int, v=True):
    instruction = str(instruction)
    pmode = instruction.zfill(5)

    p1_val = puzzle_input[i + 1] if int(pmode[2]) == 0 else (i + 1)
    p2_val = puzzle_input[i + 2] if int(pmode[1]) == 0 else (i + 2)
    p3_val = puzzle_input[i + 3] if int(pmode[0]) == 0 else (i + 3)

    if v:
        print(f"pmode={''.join(map(str, pmode))}")
        print(f"{p1_val=}, {p2_val=}, {p3_val=}")

    return p1_val, p2_val, p3_val


input_instruction = 5

i = 0
while i < len(puzzle_input):
    instruction = puzzle_input[i]
    opcode = int(str(instruction)[-1])

    p1, p2, p3 = parameter_mode(puzzle_input, instruction, i)

    if opcode == 1:
        print(f"{opcode=}")
        puzzle_input[p3] = puzzle_input[p2] + puzzle_input[p1]
        i += 4
    
    if opcode == 2:
        print(f"{opcode=}")
        puzzle_input[p3] = * puzzle_input[p2] * puzzle_input[p1]
        i += 4

    if opcode == 3:
        print(f"{opcode=}")
        puzzle_input[p1] = input_instruction
        i += 2

    if opcode == 4 or opcode == 99:
        print(f"{opcode=}")
        if puzzle_input[p1] != 0 and puzzle_input[i + 2] == 99:
            print(f"Success: {puzzle_input[p1]}")
            break
        elif puzzle_input[p1] != 0 and puzzle_input[i + 2] != 99:
            print(f"Fail: {puzzle_input[p1]}")
            break
        else:
            print(f"{puzzle_input[p1]}")
        i += 2


    # Opcode 5 jump-if-true: if the first parameter is non-zero, it sets the
    # instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    
    if opcode == 5: 
        if puzzle_input[p1] != 0:
            i = puzzle_input[p2]
        else:
            i += 3
    
    # Opcode 6 jump-if-false: if the first parameter is zero, it sets the instruction
    # pointer to the value from the second parameter. Otherwise, it does nothing.

    if opcode == 6:
        if puzzle_input[p1] == 0:
            i = puzzle_input[p2]
        else:
            i += 3

    # Opcode 7 less than: if the first parameter is less than the second parameter,
    # it stores 1 in the position given by the third parameter. Otherwise, it stores 0.

    if opcode == 7:
        if puzzle_input[p1] < puzzle_input[p2]:
            puzzle_input[p3] = 1
        else:
            puzzle_input[p3] = 0
        i += 4     

    # Opcode 8 equals: if the first parameter is equal to the second parameter,
    # it stores 1 in the position given by the third parameter. Otherwise, it stores 0.

    if opcode == 8:
        if puzzle_input[p1] == puzzle_input[p2]:
            puzzle_input[p3] = 1
        else:
            puzzle_input[p3] = 0
        i += 4  



# 1002,4,3,4,33 
# multiply instruction - rightmost two digits of the first value,
# 02, indicate opcode 2, multiplication. Then, going right to left,
# the parameter modes are 0, 1 and 0

# Parameters that an instruction writes to will never be in immediate mode.

#It is important to remember that the instruction pointer should increase by
# the number of values in the instruction after the instruction finishes.
# Because of the new instructions, this amount is no longer always 4.


#print(len(puzzle_input))
