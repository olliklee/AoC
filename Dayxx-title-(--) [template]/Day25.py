# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = '2024', '25'


def is_lock(item):
    return item[0] == 31


def convert_n_sort(puzzle):
    locks, keys = [], []
    for keylock in puzzle:
        item = [int(i, 2) for i in keylock.replace('.', '0').replace('#', '1').split('\n')]
        which = locks if is_lock(item) else keys
        which.append(item[1:-1])
    return locks, keys


def solve():
    part2 = 0
    puzzle = load_input(test=False, delimiter='\n\n')
    locks, keys = convert_n_sort(puzzle)

    part1 = sum(not any(lock[i] & key[i] for i in range(5)) for lock in locks for key in keys)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
