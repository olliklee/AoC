# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = '2016', '15'


def is_open(disc, second):
    freq, offset = disc
    return not (second - offset) % freq


def solve():
    puzzle = load_input(split_by_line=True)
    discs = {int(n): (int(freq), int(freq) - int(offset))
             for line in puzzle
             for n, freq, _, offset in [re.findall(r'(\d+)', line)]}

    # part1
    part1 = 0
    while not all(is_open(discs[d], part1 + d) for d in discs.keys()):
        part1 += 1

    # part2
    part2 = part1
    discs[max(discs.keys()) + 1] = (11, 0)
    while not all(is_open(discs[d], part2 + d) for d in discs.keys()):
        part2 += 1

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
