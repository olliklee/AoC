# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2016", "01"


def solve():
    puzzle = load_input(delimiter=', ')

    startx, starty = 0, 0
    x, y = startx, starty
    direction = 0  # 0 = N
    visited = set()
    found = False
    x_koos, y_koos = 0, 0

    for step in puzzle:
        direction = (direction + 90 if step[0] == 'R' else direction - 90) % 360
        dist = int(step[1:])
        for i in range(dist):
            if direction == 0: y -=1
            elif direction == 90: x += 1
            elif direction == 180: y += 1
            elif direction == 270: x -= 1

            if (x, y) in visited and not found:
                x_koos, y_koos = x, y
                found = True

            visited.add((x, y))

    part1 = manhattan_distance(startx, starty, x, y)
    part2 = manhattan_distance(startx, starty, x_koos, y_koos)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)


