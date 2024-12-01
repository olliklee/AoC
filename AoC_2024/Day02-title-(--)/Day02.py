# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

import re
from AoC_2024.aoc_helper import run_puzzles

year, day = "2024", "01"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final

def prepare_input(file_name):
    with open(file_name) as f:
        content = f.read()
    return content

def solve_a():
    # code here

    return 0

def solve_b():
    # code here
    return 0

### ----------- Start ------------- ###

puzzle = prepare_input(filename)

run_puzzles(day, year, solve_a, solve_b)