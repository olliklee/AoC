# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re
from itertools import combinations

year, day = "2016", "03"


def is_valid(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a


def solve():
    puzzle = load_input(test=False)
    matches = re.findall(r'(\d+) +(\d+) +(\d+)', puzzle, re.MULTILINE)
    triangles = [(int(a), int(b), int(c)) for a, b, c in matches]

    part1 = sum([is_valid(*tri) for tri in triangles])

    part2 = sum([is_valid(triangles[i][col], triangles[i + 1][col], triangles[i + 2][col]) \
                 for i in range(0, len(triangles) - 2, 3) \
                 for col in range(3)])

    return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
