# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2021", "04"


def solve():
    numbers = list(map(int, load_input().split(',')))
    part_a = part_b = 0
    haeufigkeiten = {key: numbers.count(key) for key in range(9)}

    for d in range(257):
        zero = haeufigkeiten[0]
        haeufigkeiten[0] = 0
        for key in range(1, 9):
            haeufigkeiten[key-1] += haeufigkeiten[key]
            haeufigkeiten[key] = 0

        haeufigkeiten[6] += zero
        haeufigkeiten[8] += zero
        if d == 79: part_a = sum(haeufigkeiten.values())
        if d == 255: part_b = sum(haeufigkeiten.values())

    return part_a, part_b


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
