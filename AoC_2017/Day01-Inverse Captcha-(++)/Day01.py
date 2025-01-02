# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2017", "01"


def solve():
    puzzle = load_input()
    
    part1 = sum([int(puzzle[i]) for i in range(len(puzzle)) if puzzle[i] == puzzle[(i+1) % len(puzzle)]])
    part2 = sum([int(puzzle[i]) for i in range(len(puzzle)) if puzzle[i] == puzzle[(i+len(puzzle)//2) % len(puzzle)]])

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
