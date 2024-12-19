# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = '2024', '19'


def is_valid(towel, patterns, max_size, memo=None):
    print('.', end='')
    if not towel:
        return True
    if memo is None:
        memo = {}
    if towel in memo:
        return memo[towel]

    for size in range(1, max_size + 1):
        if size > len(towel):
            break
        combi = towel[:size]
        if combi in patterns:
            if is_valid(towel[size:], patterns, max_size, memo):
                memo[towel] = True
                return True

    memo[towel] = False
    return False


def solve():
    part1 = part2 = 0

    patterns, towels = load_input(test=False).split('\n\n')

    stripes = patterns.split(', ')
    max_size = max([len(s) for s in stripes])
    towels = towels.split('\n')
    for i, towel in enumerate(towels):
        part1 += 1 if is_valid(towel, stripes, max_size) else 0
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
