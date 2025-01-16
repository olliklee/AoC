# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import run_puzzle

year, day = "2016", "18"


def calc_tile(line, pos):
    trap = ['^^.', '.^^', '^..', '..^']
    length = len(line)
    if pos == 0:
        pattern = '.' + line[:2]
    elif pos == length-1:
        pattern = line[pos-1:] + '.'
    else:
        pattern = line[pos-1:pos+2]

    return '^' if pattern in trap else '.'


def create_map(puzzle, size):
    room = [puzzle]
    for i in range(size - 1):
        room.append(''.join([calc_tile(room[-1], i) for i in range(len(puzzle))]))
    return room


def solve():
    puzzle = '^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^'
    size_pt1, size_pt2 = 40, 400000

    part1 = sum(line.count('.') for line in create_map(puzzle, size_pt1))
    part2 = sum(line.count('.') for line in create_map(puzzle, size_pt2))

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
