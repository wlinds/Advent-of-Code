def my_func(i):
    return ((int(i) // 3) - 2)

my_list = []

with open('2019/day1.txt', 'r') as file:
    for line in file:
        result = my_func(line)

        while result > 0:
            my_list.append(result)
            result = my_func(result)

print(sum(my_list))