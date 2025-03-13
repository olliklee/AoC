# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import run_puzzle

year, day = "2016", "18"


def calc_tile(line, pos):
    line = '.' + line + '.'
    return '.' if line[pos] == line[pos+2] else '^'


def generate_next_line(line):
    next_line = ''.join([calc_tile(line, i) for i in range(len(line))])
    return next_line, next_line.count('.')


def process(puzzle, size):
    line, safe_spaces = puzzle, puzzle.count('.')
    for i in range(size - 1):
        new_line, safe = generate_next_line(line)
        safe_spaces += safe
        line = new_line
    return safe_spaces


def solve():
    puzzle = '^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^'
    size_pt1, size_pt2 = 40, 400000

    part1 = process(puzzle, size_pt1)
    part2 = process(puzzle, size_pt2)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
