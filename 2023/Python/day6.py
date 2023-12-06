with open('2023/Python/data/puzzle_6.txt', 'r') as f:
        ms = [int(val) for val in next(f).split()[1:]]
        mm = [int(val) for val in next(f).split()[1:]]
        
def get_combinations(n, min_val):
    lst = []
    for i in range(n):
        j = n - i
        if i*j > min_val: lst.append((i*j))

    return len(lst)

sum = 1
for i in range(len(mm)):
    sum *= get_combinations(ms[i], mm[i])
    print(sum)

print(sum)

print(get_combinations(int(''.join(map(str, ms))), int(''.join(map(str, mm)))))