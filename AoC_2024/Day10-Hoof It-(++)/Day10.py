# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2024", "10"


def get_val(puzzle, pos):
    x, y = pos
    if 0 <= y < len(puzzle) and 0 <= x < len(puzzle[0]):
        return int(puzzle[y][x])
    return -1


def run(puzzle, pos, val, goals, visited):
    act_val = get_val(puzzle, pos)

    if val + 1 != act_val:
        return 0
    if act_val == 9:
        goals.add(pos)
        return 1
    visited.add(pos)

    x, y = pos
    neighbours = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
    ways = 0
    for neighbour in neighbours:
        if neighbour not in visited:
            ways += run(puzzle, neighbour, val+1, goals, visited)

    visited.remove(pos)
    return ways


def solve():
    part1 = part2 = 0
    puzzle = load_input(test=False, split_by_line=True)

    start_points = [(x, y) for y in range(len(puzzle)) for x in range(len(puzzle[0])) if puzzle[y][x] == '0']

    ways = 0
    for pos in start_points:
        goals = set()
        visited = set()
        ways += run(puzzle, pos, -1, goals, visited)  # `-1` als Startwert für `val`
        part1 += len(goals)
        part2 = ways

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
