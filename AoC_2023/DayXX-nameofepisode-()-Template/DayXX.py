# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

year, day = "YYYY", "XX"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = test              # change to final when ready


def prepare_input():
    with open(filename) as f:
        content = f.read().split("\n")

    return content


def solve_a():
    # code goes here
    return 0


def solve_b():
    # code goes here
    return 0

### ----------- Start ------------- ###

puzzle = prepare_input()
run_puzzles(day, year, solve_a, solve_b)
