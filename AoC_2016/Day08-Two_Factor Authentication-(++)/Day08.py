# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import deque

year, day = "2016", "08"


def execute(screen, height, width, com):
    if len(com) == 2:  # zeichne rect
        xx, yy = tuple(map(int, com[1].split('x')))
        for row in range(yy):
            for col in range(xx):
                screen[(col, row)] = '#'

    elif com[2].startswith('y'):  # verschiebe vertikal
        yy, amount = int(com[2][2:]), int(com[4])
        line = deque([screen[(position, yy)] for position in range(width)])
        line.rotate(amount)
        for position in range(width):
            screen[(position, yy)] = line[position]

    elif com[2].startswith('x'):  # verschiebe horizontal
        xx, amount = int(com[2][2:]), int(com[4])
        line = deque([screen[(xx, position)] for position in range(height)])
        line.rotate(amount)
        for position in range(height):
            screen[(xx, position)] = line[position]
    else:
        raise ValueError


def solve():
    test_input = False
    scr_height = 3 if test_input else 6
    scr_width = 7 if test_input else 50
    puzzle = load_input(test=test_input, split_by_line=True)

    screen = {(xx, yy): "." for xx in range(scr_width) for yy in range(scr_height)}

    for line in puzzle:  # executes all commands
        command = line.split(' ')
        execute(screen, scr_height, scr_width, command)

    part1 = sum([1 for _, v in screen.items() if v == '#'])

    print_matrix(screen)
    part2 = 'EOARGPHYAO'

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
