#  Solutions of Advent of Code
#  Oliver Kleemann

from time import perf_counter

from aoc_helper import *
import re

year, day = "2022", "05"


def move(stacks, order, crane_type):
    amount, f, t = order

    # lifts crates from stack
    crates_taken = stacks[f - 1][-amount:]
    stacks[f - 1] = stacks[f - 1][:-amount]

    if crane_type == "9000":
        crates_taken = crates_taken[::-1]
    elif crane_type != "9001":
        raise Exception("Unknown Crane!")

    # puts crates on target stack
    stacks[t - 1] = stacks[t - 1] + crates_taken


def init_stacks(crates):
    dimx, dimy = (len(crates[0]) + 1) // 4, len(crates)
    stacks = [[] for _ in range(dimx)]

    for line in crates[:-1]:
        for i, char in enumerate(line[1::4]):
            if char != " ":
                stacks[i].append(char)
    return [col[::-1] for col in stacks]


def solve():
    part1 = part2 = 0
    crates, commands = load_input(test=False, delimiter='\n\n')
    orders = [tuple(map(int, match)) for match in re.findall(r'(\d+) from (\d) to (\d)', commands, re.MULTILINE)]
    crates = crates.splitlines()

    # part1
    stacks = init_stacks(crates)
    for order in orders:
        move(stacks, order, crane_type="9000")
    part1 = "".join([col[-1] for col in stacks])

    # part2
    stacks = init_stacks(crates)
    for order in orders:
        move(stacks, order, crane_type="9001")
    part2 = "".join([col[-1] for col in stacks])

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
