# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2015", "16"


def get_filtered_dict(aunties_dict, known_dict, my_key):
    filtered_dict = {}
    for key, value in aunties_dict.items():
        if my_key in value.keys():
            if known_dict[my_key] == value[my_key]:
                filtered_dict[key] = value
        else:
            filtered_dict[key] = value
    return filtered_dict


def get_encabulated_dict(my_dict, known_dict, my_key):
    filtered_dict = {}
    for key, value in my_dict.items():

        if my_key not in ['cats', 'trees', 'pomeranians', 'goldfish']:
            if my_key in value.keys():
                if known_dict[my_key] == value[my_key]:
                    filtered_dict[key] = value
            else:
                filtered_dict[key] = value

        elif my_key in ['cats', 'trees']:
            if my_key in value.keys():
                if known_dict[my_key] < value[my_key]:
                    filtered_dict[key] = value
            else:
                filtered_dict[key] = value

        elif my_key in ['pomeranians', 'goldfish']:
            if my_key in value.keys():
                if known_dict[my_key] > value[my_key]:
                    filtered_dict[key] = value
            else:
                filtered_dict[key] = value

    return filtered_dict


def solve():
    part1 = part2 = 0
    puzzle = (load_input()
              .replace(":", "")
              .replace(",", "").split('\n'))

    aunties_dict = {}
    for line in puzzle:
        line = line.split(" ")
        aunties_dict[int(line[1])] = {line[2]: int(line[3]), line[4]: int(line[5]), line[6]: int(line[7])}

    known_dict = {'children': 3, 'cats': 7,
                  'samoyeds': 2, 'pomeranians': 3,
                  'akitas': 0, 'vizslas': 0,
                  'goldfish': 5, 'trees': 3,
                  'cars': 2, 'perfumes': 1}

    filtered_aunties = aunties_dict
    for key in known_dict.keys():
        filtered_aunties = get_filtered_dict(filtered_aunties, known_dict, key)
        if len(filtered_aunties) == 1:
            part1 = list(filtered_aunties)[0]
            break

    filtered_aunties = aunties_dict
    for key in known_dict.keys():
        filtered_aunties = get_encabulated_dict(filtered_aunties, known_dict, key)
        if len(filtered_aunties) == 1:
            part2 = list(filtered_aunties)[0]
            break

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
