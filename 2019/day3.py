# Manhattan path

# Two wires are connected to a central port and extend outward on a grid.
# You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

"""
R8,U5,L5,D3: from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........

Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........

These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

"""


# What is the Manhattan distance from the central port to the closest intersection?

with open('2019/day3.txt', 'r') as file:
    two_rows = file.read()

wires = two_rows.split('\n')
a_path = wires[0].split(',')
b_path = wires[1].split(',')

print(len(a_path))
print(len(b_path))

head_a = [0,0] #R995, D882, R114 ...
head_b = [0,0] #L999, D22, L292 ....

import re

def get_coordinate(instruction: str):

    if instruction[0] == "R":
        direction, phase = "x", "+"
    elif instruction[0] == "L":
        direction, phase = "x", "-"
    elif instruction[0] == "U":
        direction, phase = "y", "+"
    elif instruction[0] == "D":
        direction, phase = "y", "-"

    value = re.sub(r'\D', '', instruction)
    return direction, phase, value

import matplotlib.pyplot as plt

def draw_lines(wire, start_x=0, start_y=0):
    x_coords = [start_x]
    y_coords = [start_y]

    for instruction in wire:
        direction, phase, value = get_coordinate(instruction)

        if direction == 'x':
            x = int(value)
            if phase == '-':
                x = -x
            start_x += x
            x_coords.append(start_x)
            y_coords.append(start_y)
        elif direction == 'y':
            y = int(value)
            if phase == '-':
                y = -y
            start_y += y
            y_coords.append(start_y)
            x_coords.append(start_x)

    return x_coords, y_coords

# wire a
a_x_coords, a_y_coords = draw_lines(a_path, head_a[0], head_a[1])
plt.plot(a_x_coords, a_y_coords, label='Wire Path A')

# wire b
b_x_coords, b_y_coords = draw_lines(b_path, head_b[0], head_b[1])
plt.plot(b_x_coords, b_y_coords, label='Wire Path B')

plt.title('Wire Paths')
plt.legend()
plt.grid(True)
plt.savefig("day_3_wires.png")
plt.show()