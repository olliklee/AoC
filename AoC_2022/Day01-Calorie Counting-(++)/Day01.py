#  Solutions of Advent of Code
#  Oliver Kleemann

from aoc_helper import *

year, day = "2022", "01"


def solve():
    puzzle = load_input(delimiter='\n\n')
    
    calories = sorted([sum(map(int, elf.split('\n'))) for elf in puzzle], reverse=True)
    
    part1 = calories[0]
    part2 = sum(calories[0:3])
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
