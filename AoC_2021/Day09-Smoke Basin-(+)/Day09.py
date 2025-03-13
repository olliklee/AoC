# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2021", "09"


def value_at(pos, data):
    return int(data[pos[1] - 1][pos[0] - 1])


def is_lowest_point(pos, data):
    x, y = pos
    value = value_at(pos, data)
    neighbour_up = 9 if y < 2 else int(data[y - 2][x - 1])
    neighbour_down = 9 if y > len(data) - 1 else int(data[y][x - 1])
    neighbour_left = 9 if x < 2 else int(data[y - 1][x - 2])
    neighbour_right = 9 if x > len(data[0]) - 1 else int(data[y - 1][x])
    lowest_neighbours = min([neighbour_up, neighbour_down, neighbour_right, neighbour_left])
    return value < lowest_neighbours


def get_deepest_points(data):
    return [(col, row)
            for col in range(1, len(data) + 1)
            for row in range(1, len(data[0]) + 1)
            if is_lowest_point((row, col), data)]


def solve():
    part2 = 0
    puzzle = [list(line) for line in load_input(split_by_line=True)]

    part1 = sum([value_at((row, col), puzzle) + 1
                 for col in range(1, len(puzzle) + 1)
                 for row in range(1, len(puzzle[0]) + 1)
                 if is_lowest_point((row, col), puzzle)])

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)

# def solve_09b():
#     riddle = read_input_from_file("input_test.txt")
#
#     basin_points = []
#     deepest_points = get_deepest_points(riddle)
#     for point in deepest_points:
#         basin_points = get_basin_size(point, data)
