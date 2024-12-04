# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2021", "06"


def solve():
    numbers = list(map(int, load_input().split(',')))

    part_a = part_b = 0
    freq = {key: numbers.count(key) for key in range(9)}

    for d in range(257):
        zero = freq[0]
        freq[0] = 0
        for key in range(1, 9):
            freq[key-1] += freq[key]
            freq[key] = 0

        freq[6] += zero
        freq[8] += zero
        if d == 79: part_a = sum(freq.values())
        if d == 255: part_b = sum(freq.values())

    return part_a, part_b


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
