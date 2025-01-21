# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2022", "14"


def sand_move(walls, sand, limit, pos=(500, 0)):
    dirs = [(0, 1), (-1, 1), (1, 1)]
    if pos in walls or pos in sand or pos[1] > limit:
        return

    x, y = pos
    for direction in dirs:
        dx, dy = direction
        new_pos = (x + dx, y + dy)
        if new_pos not in walls and new_pos not in sand:
            return sand_move(walls, sand, limit, new_pos)

    sand.add(pos)
    return


def create_walls(puzzle):
    walls = set()
    for line in puzzle:
        construct = line.split(' -> ')
        for i in range(len(construct) - 1):
            x1, y1, x2, y2 = list(map(int, ','.join([construct[i], construct[i + 1]]).split(',')))
            if x1 == x2:
                start, stop = (y1, y2 + 1) if y1 < y2 else (y2, y1 + 1)
                for y in range(start, stop):
                    walls.add((x1, y))
            elif y1 == y2:
                start, stop = (x1, x2 + 1) if x1 < x2 else (x2, x1 + 1)
                for x in range(start, stop):
                    walls.add((x, y1))
    return walls


def solve():
    puzzle = load_input(split_by_line=True)
    walls = create_walls(puzzle)
    abyss = max(y for _, y in walls)

    # part1
    sand = set()
    for _ in range(1000):
        sand_move(walls, sand, limit=abyss)
    part1 = len(sand)

    # part2
    # add the additional floor
    for x in range(300, 800):
        walls.add((x, abyss + 2))

    for _ in range(30000):
        sand_move(walls, sand, limit=abyss + 2)
    part2 = len(sand)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
