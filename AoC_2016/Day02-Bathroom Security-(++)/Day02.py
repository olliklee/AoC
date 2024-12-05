# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = '2016', '02'


def get_value(x, y, grid):
    return grid[y][x]


def solve():
    puzzle = load_input(test=False, split_by_line=True)
    part1 = part2 = ''
    delta = dict(U=(0, -1), D=(0, 1), L=(-1, 0), R=(1, 0))

    pad1 = [('1', '2', '3'),
            ('4', '5', '6'),
            ('7', '8', '9')]
    pad2 = [('', '', '1', '', ''),
            ('', '2', '3', '4', ''),
            ('5', '6', '7', '8', '9'),
            ('', 'A', 'B', 'C', ''),
            ('', '', 'D', '', '')]

    x, y = 1, 1
    for line in puzzle:
        for step in line:
            x = clamp(x + delta[step][0], 0, 2)
            y = clamp(y + delta[step][1], 0, 2)
        part1 += get_value(x, y, pad1)

    x, y = 0, 2
    for line in puzzle:
        for step in line:
            x_new = clamp(x + delta[step][0], 0, 4)
            y_new = clamp(y + delta[step][1], 0, 4)
            if get_value(x_new, y_new, pad2):
                x, y = x_new, y_new

        part2 += get_value(x, y, pad2)

    return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
