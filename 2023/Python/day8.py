with open('2023/Python/data/puzzle_8.txt', 'r') as f:
    direction = next(f).strip()
    rows = []

    for line in f:
        parts = line.split('=')
        if len(parts) == 2:
            left = parts[0].strip()
            right = ["".join(filter(str.isalpha, part)) for part in parts[1].split(',')]
            right.insert(0, left)
            rows.append(right)

direction = direction * 4
step = 0
target = "AAA"
while target != "ZZZ":
    for i in range(len(direction)):
        idx = 1
        if direction[i] == "R":
            idx=2
        for row in rows:
            if row[0] == target:
                target = row[idx]
                step +=1
                break
        if target == "ZZZ":
            break

print(step)



