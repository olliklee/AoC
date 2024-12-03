# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2024.aoc_helper import *

import re

year, day = "2024", "01"


def solve_a():
    return sum([abs(left_col[i] - right_col[i]) for i in range(len(left_col))])

def solve_b():
    return sum([left_col[i] * right_col.count(left_col[i]) for i in range(len(left_col))])


### ----------- Start ------------- ###

puzzle =  load_input(day, test=False)

left_col = sorted(list(map(int, re.findall(r'^\d+', puzzle, re.MULTILINE))))
right_col = sorted(list(map(int, re.findall(r'\d+$', puzzle, re.MULTILINE))))

run_puzzles(day, year, solve_a, solve_b)