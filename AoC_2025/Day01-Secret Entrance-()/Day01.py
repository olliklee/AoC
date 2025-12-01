# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import deque

year, day = "2025", "01"


def solve():
    part1 = part2 = 0
    puzzle = load_input(test=True, split_by_line=True)
    dq = deque(range(100))
    dq.rotate(50)

    for row in puzzle:
        direction = row[0]
        shift = int(row[1:])

        if direction == "R":
            shift *= -1

        wraps = abs(shift) // len(dq)

        dq.rotate(shift)
        print(f'{row:6}, {shift:6}, {dq[0]:5}, {wraps:6}')
        part2 += wraps

        if dq[0] ==  0:
            part1 += 1


    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)


#falsch: 6364