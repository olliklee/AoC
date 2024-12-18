# # #  Solutions of Advent of Code
# # #  Oliver Kleemann
from aoc_helper import *
from itertools import combinations

day = '05'
year = '2024'


def is_valid(line, pairs):
    for l, r in combinations(line, 2):
        if (l, r) not in pairs: return False
    return True

def bubble_sort(line, pairs):
    while not is_valid(line, pairs):
        for l, r in combinations(line, 2):
            if (l, r) not in pairs:
                line[line.index(r)], line[line.index(l)] = l, r
    return line

def solve():
    puzzle = load_input(test=False, split_by_line=True)

    pairs = set()
    bad_lines = []
    good_lines = []

    # prepare input
    for line in puzzle:
        if '|' in line:
            l, r = line.split('|')
            pairs.add((int(l), int(r)))
        elif ',' in line:
            line = list(map(int, line.split(',')))
            (good_lines if is_valid(line, pairs) else bad_lines).append(line)

    part1 = sum(line[len(line) // 2] for line in good_lines)
    part2 = sum([line[len(bubble_sort(line, pairs)) // 2] for line in bad_lines])

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)