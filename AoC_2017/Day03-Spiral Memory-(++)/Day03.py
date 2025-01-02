# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict

year, day = "2017", "03"


def sum_of_neighbors(grid, koos):
    y, x = koos
    neighbours = [(1, 1), (1, -1), (-1, -1), (-1, 1), (0, 1), (-1, 0), (0, -1), (1, 0)]
    return sum([grid[(x + n[0], y + n[1])]
                for n in neighbours
                if grid[(x + n[0], y + n[1])]])


def generate_spiral(center, n, version):
    if n % 2 == 0:
        raise ValueError("n muss eine ungerade Zahl sein.")

    spiral = defaultdict(int)

    x, y = center
    num = 1
    spiral[(x, y)] = num
    num += 1

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    direction = 0
    step_size = 1

    while num <= n:
        for _ in range(2):
            for _ in range(step_size):

                dx, dy = directions[direction]
                x, y = x + dx, y + dy

                if version == 1:
                    spiral[(y, x)] = num
                    num += 1

                elif version == 2:
                    value = sum_of_neighbors(spiral, (x, y))
                    spiral[(y, x)] = value
                    if value >= n:
                        return spiral

            direction = (direction + 1) % 4
        step_size += 1
    return spiral


def solve():
    puzzle = 347991
    center = (0, 0)

    spiral = generate_spiral(center, puzzle, 1)
    x, y = next((key for key, val in spiral.items() if val == puzzle))
    part1 = abs(x) + abs(y)

    spiral = generate_spiral(center, puzzle, 2)
    part2 = max(spiral.values())

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
