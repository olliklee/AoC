# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict

year, day = "2015", "03"

DIRS = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}


def get_new_pos(pos, direction):
    x, y = pos
    delta_x, delta_y = DIRS[direction]
    return x + delta_x, y + delta_y


def solve():
    puzzle = load_input()
    
    houses = set()
    pos = (0, 0)
    for direction in puzzle:
        houses.add(pos)
        pos = get_new_pos(pos, direction)
    part1 = len(houses)
    
    houses.clear()
    pos, rpos = (0, 0), (0, 0)
    for i, direction in enumerate(puzzle):
        if i % 2 == 0:
            houses.add(pos)
            pos = get_new_pos(pos, direction)
        else:
            houses.add(rpos)
            rpos = get_new_pos(rpos, direction)
    part2 = len(houses)
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
