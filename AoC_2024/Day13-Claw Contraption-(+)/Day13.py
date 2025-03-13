# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2024", "13"

def check_win_and_cost(puzzle, machine):
    ax, ay, bx, by, px, py = machine
    ca, cb = 3, 1
    for a in range(101):
        val_ax = a * ax
        possible = (val_ax + 100 * bx) >= px >= val_ax + bx
        if possible:
            for b in range(100, -1, -1):
                val_bx = b * bx
                if val_ax + val_bx == px:
                    if a * ay + b * by == py:
                        return a * ca + b * cb


    return 0

def solve():
    part1 = part2 = 0

    puzzle = load_input(test=False).split('\n\n')
    machines = []

    for machine in puzzle:
        numbers = map(int, re.findall(r'\d+', machine))
        machines.append(numbers)

    for machine in machines:
        part1 += check_win_and_cost(puzzle, machine)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
