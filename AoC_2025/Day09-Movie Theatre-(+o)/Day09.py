# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import run_puzzle, load_input, manhattan_distance
from itertools import combinations

year, day = "2025", "09"


def area(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return abs(x1-x2) * abs(y1-y2) + abs(x1-x2) + abs(y1-y2) + 1


def solve():
    part2 = 0
    puzzle = load_input(test=True, split_by_line=True)
    red = {tuple(map(int, line.split(','))): "#" for line in puzzle}

    areas = combinations(red.keys(), 2)

    max_distance = max_area = 0

    for a, b in areas:
        distance = manhattan_distance(*a, *b)
        if max_distance <= distance:
            max_area = max(max_area, area(a, b))
            max_distance = distance

    part1 = max_area
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)


# x1, y1 = 2,5
# x2, y2 = 11, 1
# area = 50
# area = abs(x1-x2) * abs(y1-y2) +abs(x1-x2) + abs(y1-y2) + 1
