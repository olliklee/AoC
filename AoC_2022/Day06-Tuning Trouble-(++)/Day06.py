# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2022", "06"


def characters(signal, pl):
    return [i + pl for i in range(len(signal) - pl) if len(set(signal[i:i + pl])) == pl][0]


def solve():
    signal = load_input()

    part1 = characters(signal, 4)
    part2 = characters(signal, 14)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
