# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import numpy as np
import re

year, day = "2015", "06"

SHAPE = (1000, 1000)


def solve():
    puzzle = load_input()
    pattern = r'(toggle|off|on|) (\d+),(\d+) through (\d+),(\d+)'
    puzzle = [(com, int(x1), int(y1), int(x2), int(y2)) for com, x1, y1, x2, y2 in re.findall(pattern, puzzle, re.MULTILINE)]

    matrix1 = np.full(SHAPE, False)
    matrix2 = np.zeros(SHAPE)
    for command in puzzle:
        com, x1, y1, x2, y2 = command
        area1 = matrix1[x1:x2 + 1, y1:y2 + 1]
        area2 = matrix2[x1:x2 + 1, y1:y2 + 1]
        if com == 'toggle':
            area1[:] = np.logical_not(area1)
            area2 += 2
        elif com == 'off':
            area1[:] = False
            area2 -= 1
            area2[area2 < 0] = 0  # <= 0 ist bereits ausgeschaltet
        elif com == 'on':
            area1[:] = True
            area2 += 1

    part1 = np.count_nonzero(matrix1)
    part2 = int(np.sum(matrix2))

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
