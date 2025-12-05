# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2015", "18"


def new_state(matrix, position: tuple[int, int]) -> str:
    xpos, ypos = position
    neighbours = [(xpos + 1, ypos), (xpos + 1, ypos + 1), (xpos + 1, ypos - 1), (xpos, ypos - 1), (xpos, ypos + 1),
                  (xpos - 1, ypos), (xpos - 1, ypos + 1), (xpos - 1, ypos - 1)]
    if matrix.get(position, ".") == "#":
        count = sum([matrix.get(neighbour, ".") == "#" for neighbour in neighbours])
        return "#" if count in [2, 3] else "."
    else:
        count = sum([matrix.get(neighbour, ".") == "#" for neighbour in neighbours])
        return "#" if count == 3 else "."


def light_corners(matrix):
    corners = [(0, 0), (0, 99), (99, 0), (99, 99)]
    for corner in corners:
        matrix[corner] = '#'


def solve():
    testinput = False
    loops = 4 if testinput else 100
    puzzle = load_input(test=testinput)

    initial_matrix = text_to_dictmap(puzzle)

    # part 1
    new_matrix = initial_matrix.copy()
    last_matrix = new_matrix.copy()
    for i in range(loops):
        for position, state in last_matrix.items():
            new_matrix[position] = new_state(last_matrix, position)
        last_matrix = new_matrix.copy()

    part1 = sum([1 for position, state in last_matrix.items() if state == '#'])

    # part 2
    new_matrix = initial_matrix.copy()
    last_matrix = new_matrix.copy()
    light_corners(last_matrix)
    for i in range(loops):
        for position, state in last_matrix.items():
            new_matrix[position] = new_state(last_matrix, position)
        last_matrix = new_matrix.copy()
        light_corners(last_matrix)

    part2 = sum([1 for position, state in last_matrix.items() if state == '#'])

    return part1, part2


# ----------   Start   ----------   #

run_puzzle(day, year, solve)
