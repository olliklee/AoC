# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict

year, day = "2015", "07"

wire_dict = defaultdict(int)


def calculate(wire, commands, values):
    try:
        value = int(wire)
        values[wire] = value
        return
    except ValueError:
        pass
    command = commands[wire]

    if len(command) == 1:
        try:
            values[wire] = int(command[0])
        except ValueError:
            calculate(command[0], commands, values)
            values[wire] = values[command[0]]

    elif len(command) == 2:
        if command[0] == 'NOT':
            left = command[1]
            if values.get(left) is None:
                calculate(left, commands, values)
                values[wire] = ~values[left]

    elif len(command) == 3:
        left = command[0]
        right = command[2]
        operator = command[1]
        if values.get(left) is None:
            calculate(left, commands, values)
        if values.get(right) is None:
            calculate(right, commands, values)
        if operator == "LSHIFT":
            values[wire] = values[left] << values[right]
        elif operator == "RSHIFT":
            values[wire] = values[left] >> values[right]
        elif operator == "AND":
            values[wire] = values[left] & values[right]
        elif operator == "OR":
            values[wire] = values[left] | values[right]


def solve():
    puzzle = [line.split() for line in load_input(split_by_line=True)]
    connect_dict = {order[-1]: order[:-2] for order in puzzle}

    values = {}
    calculate("a", connect_dict, values)
    part1 = values['a']
    print(part1)

    values = {}
    connect_dict['b'] = [part1]
    calculate('a', connect_dict, values)
    part2 = values['a']

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)

'''
Results from AoC 2015 - Day 07
    ----------------------------------
      Part 1: 956 (0.037621 ms)
      Part 2: 40149 (0.065671 ms)
    ----------------------------------
      Time complete: 0.103292 ms'''
