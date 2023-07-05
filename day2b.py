with open("2019/day2.txt", "r") as file:
    list = [int(i) for i in file.read().split(",")]

opcodes = [1, 2, 99]

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

int_comp(list)