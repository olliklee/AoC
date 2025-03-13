# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2015", "02"


def solve():
    part1 = part2 = 0
    puzzle = load_input(split_by_line=True)
    
    for line in puzzle:
        w, l, h = map(int, line.split("x"))
        part1 += 2 * w * l + 2 * h * l + 2 * w * h \
                 + min(w * l, h * l, w * h)
        
    for line in puzzle:
        w, l, h = map(int, line.split("x"))
        smallest = sorted((w, l, h))[:2]
        part2 += w * l * h + 2 * sum(smallest)
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
