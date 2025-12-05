# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import deque

year, day = "20xx", "xx"


def solve():
    part1 = part2 = 0
    elfs = deque()
    puzzle =  3018458
    # for i in range(puzzle):
    #     elfs.append((i,1))
    #
    # while (l := len(elfs)) > 1:
    #     takes = elfs.popleft()  # Nimmt den ersten Elf
    #     gives = elfs.popleft()  # Nimmt den zweiten Elf
    #     elfs.append((takes[0], takes[1] + gives[1]))
    # part1 = elfs[0][0]+1
    # print(part1)

    # Josephus problem
    power = 1
    while power * 2 <= puzzle:
        power *= 2
    part1 = (puzzle - power) * 2 + 1

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)