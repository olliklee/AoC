# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2025", "01"


def solve():
    part1 = part2 = 0
    puzzle = load_input(test=True, split_by_line=True)
    position = 50

    for row in puzzle:
        direction = row[0]
        rotation = int(row[1:])

        if direction == "L":
            rotation *= -1

        position += rotation

        hits_zero = abs(position // 100)

        part2 += hits_zero
        position = position % 100

        if position == 0:
            part1 += 1



    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)


#falsch: 6364