# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2024", "xx"


def solve():
    part1 = part2 = 0
    puzzle1 = list(map(int, load_input(split_by_line=True)))
    puzzle2 = puzzle1[:]

    pos = 0
    while pos < len(puzzle1):
        part1 += 1
        jmp = puzzle1[pos]
        puzzle1[pos] += 1
        pos += jmp

    pos = 0
    while pos < len(puzzle2):
        part2 += 1
        jmp = puzzle2[pos]
        puzzle2[pos] += -1 if puzzle2[pos] >= 3 else +1
        pos += jmp

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
