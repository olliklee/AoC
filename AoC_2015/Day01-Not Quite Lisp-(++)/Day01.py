# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2015", "01"


def solve():
    puzzle = load_input()
    part1 = puzzle.count("(") - puzzle.count(")")

    part2 = floor = 0
    while floor != -1:
        part2 += 1
        letter = puzzle[part2 - 1]
        if letter == "(":
            floor += 1
        elif letter == ")":
            floor -= 1
        else:
            print("Error")


    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
