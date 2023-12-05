# food production problem | # seed-to-location map

# The almanac (your puzzle input) lists all of the seeds that need to be planted. 
#  - what type of soil to use with each kind of seed
#  - what type of fertilizer to use with each kind of soil,
#  - what type of water to use with each kind of fertilizer, and so on.
# 
# Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category 
# - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

# 52 50 48

# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

# The rest of the almanac contains a list of maps which describe how to
# convert numbers from a source category into numbers in a destination category.

# seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination).

# Rather than list every source number and its corresponding destination number one by one,
# the maps describe entire ranges of numbers that can be converted.


def get_seeds_and_maps():
    seeds = []
    maps = []
    current_map = None

    with open('2023/Python/data/puzzle_5.txt', 'r') as f:
        seeds = next(f).split(': ')[1]
        seeds = list(map(int, seeds.split()))

        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.endswith(':'):
                if current_map:
                    maps.append({
                        'name': current_map['name'],
                        'values': current_map['values']
                    })
                current_map = {'name': line, 'values': []}
            else:
                values = list(map(int, line.split()))
                current_map['values'].append(list(map(int, values)))

        if current_map:
            maps.append({
                'name': current_map['name'],
                'values': current_map['values']
            })
    return seeds, maps

seeds, maps = get_seeds_and_maps()


# destination range start, source range start, range length.

line_1 = [[98, 99],[50,51]]
# line_2 = [[50, 51, ... 98],[52, 53, ... 100]]

def get_ranges_from_source(maps):

    result_dicts = []

    for m in maps:
        print(m.get("name"))
        length = len(m.get('values'))
        print(f"{length=}")
        print(m)

        result_dict = {'name': m.get("name"), 'ranges': []}
        
        for i in range(length):
            destin_start = m.get('values')[i][0]
            source_start = m.get('values')[i][1]
            range_length = m.get('values')[i][2]
            # print(destination_start)
            # print(source_start)
            # print(range_length)

            end_dest = destin_start + range_length
            end_src = source_start + range_length
            print(end_dest)
            assert end_dest > destin_start, "foo"

            result_dict['ranges'].append([source_start, end_src, destin_start, end_dest])

        result_dicts.append(result_dict)
    return result_dicts


ranges = get_ranges_from_source(maps)

print(ranges)



def match_seeds(seeds, ranges):
    matched_values = []

    for seed in seeds:
        matched_seed = None

        for r in ranges:
            if r[0] <= seed <= r[1]:
                matched_seed = r[2] + (seed - r[0])
                break

        if matched_seed is not None:
            matched_values.append(matched_seed)
        else:
            # Unmatched seeds
            matched_values.append(seed)

    return matched_values

#match_seeds(seeds, ranges)

print()
first_map = ranges[0].get('ranges')


new_seeds = match_seeds(seeds, first_map)
print()
print(new_seeds)

for i, _ in enumerate(ranges):
    map_iter = ranges[i].get('ranges')
    seeds = match_seeds(seeds, map_iter)

print(min(seeds))

# source range start: 98, range: 2 = source = 98,99
# destination range start: 50, range: 2 = desination 50,51

# == source 98 = destination 50

# print(maps)

# for i in maps:
#     print(i.get("name"))

# print(seeds)