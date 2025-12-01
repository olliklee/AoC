# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2025", "01"


def solve():
    part1 = part2 = 0
    puzzle = load_input(test=False, split_by_line=True)
    position = 50

    for row in puzzle:
        rotation = -int(row[1:]) if row[0] == "L" else int(row[1:])
        position += rotation

        corrector = abs(position // 100)

        print(corrector, end=" ")
        position %= 100
        print(position)

        if position == 0:
            part1 += 1

        part2 += corrector


    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
