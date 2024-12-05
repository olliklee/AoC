# # #  Solutions of Advent of Code
# # #  Oliver Kleemann
# # #  Inspired by https://www.youtube.com/watch?v=QrCdNT9PJDY
# # #  from Bradley Sward

from aoc_helper import *

year, day = '2021', '11'


def prepare_input():
    datei = load_input(split_by_line=True)
    datei = [[int(v) for v in y] for y in datei]
    return datei


def raise_by_one(data):
    new_data = [[v + 1 for v in y] for y in data]
    return new_data


def get_value(grid, row, col):
    if not (0 <= row < len(grid)) or not (0 <= col < len(grid[row])):
        return -1
    return grid[row][col]


def sum_all_values(data):
    return sum(sum(data, []))


def count_flashes(data):
    counter = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] > 9:
                counter += 1
                data[x][y] = -99999
                surroundings = [[x - 1, y], [x + 1, y], [x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y + 1],
                                [x, y + 1], [x + 1, y + 1]]
                for point in surroundings:
                    if get_value(data, *point) != -1:
                        data[point[0]][point[1]] += 1
    return counter


def reset_matrix(data):
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] < 0:
                data[x][y] = 0


def part1():
    riddle = prepare_input()
    steps = 100
    result = 0
    for _ in range(steps):
        riddle = raise_by_one(riddle)
        flashes = count_flashes(riddle)
        while flashes > 0:
            result += flashes
            flashes = count_flashes(riddle)

        reset_matrix(riddle)

    return result


def part2():
    riddle = prepare_input()
    steps = 0
    result = 0
    while sum_all_values(riddle) != 0:
        riddle = raise_by_one(riddle)
        flashes = count_flashes(riddle)
        while flashes > 0:
            result += flashes
            flashes = count_flashes(riddle)

        reset_matrix(riddle)
        steps += 1

    return steps

run_puzzles(day, year, part1, part2)
