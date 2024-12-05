# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from itertools import combinations
year, day = "2024", "02"

def check(values):
    diffs = [values[i] - values[i + 1] for i in range(len(values) - 1)]
    return all(0 < diff < 4 for diff in diffs) or \
    all(-4 < diff < 0 for diff in diffs)

def solve():
    result_a = result_b = 0
    puzzle = load_input(test=False, split_by_line=True)

    for line in puzzle:
        value_list = list(map(int, line.split()))

        result_a += check(value_list)

        combis = combinations(value_list, len(value_list) - 1)
        result_b += any(check(combi) for combi in combis)

    return result_a, result_b


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
