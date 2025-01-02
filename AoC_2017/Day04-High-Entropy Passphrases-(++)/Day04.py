# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from itertools import combinations

year, day = "2017", "04"


def is_valid_1(passphrase):
    words = passphrase.split()
    for a, b in combinations(words, 2):
        if a == b:
            return False
    return True


def is_valid_2(passphrase):
    words = passphrase.split()
    for a, b in combinations(words, 2):
        if sorted(a) == sorted(b):
            return False
    return True


def solve():
    puzzle = load_input(split_by_line=True)

    part1 = sum([1 for line in puzzle if is_valid_1(line)])
    part2 = sum([1 for line in puzzle if is_valid_2(line)])

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
