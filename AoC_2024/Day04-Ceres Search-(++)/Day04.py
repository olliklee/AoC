# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2024", "04"


def turn(text):
    matrix = [list(line) for line in text.splitlines()]
    rotated_matrix = [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]
    rotated_text = '\n'.join(''.join(row) for row in rotated_matrix)

    return rotated_text


def get_diagonals(text):
    lines = text.splitlines()
    rows, cols = len(lines), len(lines[0])

    diagonals = []
    for d in range(rows + cols - 1):
        diagonal = []
        for row in range(max(0, d - cols + 1), min(rows, d + 1)):
            col = d - row
            diagonal.append(lines[row][col])
        diagonals.append(''.join(diagonal))

    return '\n'.join(diagonals)


def check_surrounders(matrix, row, col):
    positions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    letters = ''.join([matrix[pos[0] + row][pos[1] + col] for pos in positions])
    return letters in ('MMSS', 'SSMM', 'SMSM', 'MSMS')


def solve():
    puzzle1 = load_input(test=False)
    puzzle2 = puzzle1.split('\n')

    # put all rows in any rotation into a long string with '.' as delimiter
    # and search for XMAS forward and backwards through the textline
    one_line = ''
    for _ in range(2):
        one_line += puzzle1.replace('\n', '.') + "." + get_diagonals(text=puzzle1).replace('\n', '.')
        puzzle1 = turn(puzzle1)

    matches = re.findall(r'XMAS', one_line) + re.findall(r'SAMX', one_line)
    part1 = len(matches)

    # go through the matrix without the outer rows and cols
    # check every field inside the boundaries, if it's an 'A' and the surrounders fit the pattern
    part2 = 0
    for row in range(1, len(puzzle2) - 1):
        for col in range(1, len(puzzle2[0]) - 1):
            if puzzle2[row][col] == 'A':
                part2 += check_surrounders(puzzle2, row, col)  # True = 1

    return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
