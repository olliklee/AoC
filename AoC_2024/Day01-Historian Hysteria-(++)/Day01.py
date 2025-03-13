# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

import re

year, day = "2024", "01"


def solve():
    puzzle = load_input(test=False)

    left_col = sorted(list(map(int, re.findall(r'^\d+', puzzle, re.MULTILINE))))
    right_col = sorted(list(map(int, re.findall(r'\d+$', puzzle, re.MULTILINE))))

    part1 = sum([abs(left_col[i] - right_col[i]) for i in range(len(left_col))])
    part2 = sum([left_col[i] * right_col.count(left_col[i]) for i in range(len(left_col))])

    return part1, part2

#  ----------   Start   ----------   #

run_puzzle(day, year, solve)