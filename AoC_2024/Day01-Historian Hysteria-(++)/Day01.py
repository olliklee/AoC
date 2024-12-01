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
    return sum([abs(left_col[i] - right_col[i]) for i in range(len(left_col))])

def solve_b():
    return sum([left_col[i] * right_col.count(left_col[i]) for i in range(len(left_col))])


### ----------- Start ------------- ###

puzzle = prepare_input(filename)

left_col = sorted(list(map(int, re.findall(r'^\d+', puzzle, re.MULTILINE))))
right_col = sorted(list(map(int, re.findall(r'\d+$', puzzle, re.MULTILINE))))

run_puzzles(day, year, solve_a, solve_b)