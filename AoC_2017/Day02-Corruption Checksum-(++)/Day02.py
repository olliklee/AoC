# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from itertools import combinations

year, day = "2024", "xx"


def solve():
    part1 = part2 = 0
    puzzle = load_input(split_by_line=True)
    for line in puzzle:
        line = list(map(int, line.split('\t')))
        part1 += max(line) - min(line)
        for a, b in combinations(line,2):
            if a % b == 0 :
                part2 += a // b
            elif b % a == 0:
                part2 += b // a
            else:
                continue
            break
    
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
