# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import Counter

year, day = "2016", "05"


def solve():
    puzzle = load_input(test=False, split_by_line=True)

    rotated = [[ch[i] for ch in puzzle] for i in range(len(puzzle[0]))]
    part1 = ''.join([Counter(lst).most_common(1)[0][0] for lst in rotated])
    part2 = ''.join([Counter(lst).most_common()[-1][0] for lst in rotated])

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
