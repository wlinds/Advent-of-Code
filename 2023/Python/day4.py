def puzzle_importer(file="2023/Python/data/puzzle_4.txt"):
    with open(file, 'r') as f:
        puzzle_string = f.read()
        return puzzle_string.split('\n')

a = puzzle_importer()
print(a[0])

total_points = 0

for input_string in a:
    card_number, cards_data = input_string.split(":")

    cards_list = [set(map(int, card.split())) for card in cards_data.split('|')]
    win, my = cards_list

    print(win)
    print(my)

    common = len(win & my)
    
    if common == 0:
        pass
    elif common == 1:
        total_points += 1
    else:
        total_points += 2 ** (common - 1)

print(total_points)