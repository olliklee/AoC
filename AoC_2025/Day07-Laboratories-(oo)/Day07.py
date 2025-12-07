# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2025", "07"


def advance_beam(matrix, position):
    if position is None:
        return None

    x, y = position
    new_pos = (x, y + 1)
    if new_pos not in matrix:
        return None

    if matrix[new_pos] == '.':
        matrix[new_pos] = '|'
        return advance_beam(matrix, new_pos)

    if matrix[new_pos] == '^':
        new_l, new_r = (x - 1, y), (x + 1, y)
        if new_l in matrix and matrix[new_l] == '.':
            advance_beam(matrix, new_l)
        if new_r in matrix and matrix[new_r] == '.':
            advance_beam(matrix, new_r)

    return None


def solve():
    part1 = part2 = 0
    puzzle = load_input(test=False)
    matrix = text_to_dictmap(puzzle)

    start = [pos for pos, value in matrix.items() if value == 'S'][0]
    splitter = [pos for pos, value in matrix.items() if value == '^']

    new_pos = advance_beam(matrix, start)
    advance_beam(matrix, new_pos)

    # count all splitters who were hit by a beam
    # ..|..       .|.|.
    # .|^|. hit   .|^|. failed

    for position in splitter:
        x, y = position
        part1 += matrix.get((x, y - 1), '.') == '|'

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
