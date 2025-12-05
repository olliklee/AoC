# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2017", "09"


def remove_exclamations(line):
    new_line = []
    i = 0
    while i < len(line):
        if line[i] == '!':
            i += 2
        else:
            new_line.append(line[i])
            i += 1
    return new_line


def solve():
    puzzle = load_input(test=True)
    
    puzzle = remove_exclamations(puzzle)
        
        
        
    print(''.join(new_puzzle))
    part1 = 0
    part2 = 0

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
