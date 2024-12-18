# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

from collections import defaultdict

year, day = "2023", "11"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final              # change to final when ready


def prepare_input():
    with open(filename) as f:
        content = f.read().split("\n")

    counter = 0
    converted_content = []
    for row in content:
        row_list = list(row)
        new_row = []
        for column in row_list:
            if column == '.':
                new_row.append(0)
            else:
                counter += 1
                new_row.append(counter)
        converted_content.append(new_row)

    return converted_content


def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]


def expand_universe_horizontal(matrix):
    expanded = []
    for line in matrix:
        if all(num == 0 for num in line):
            expanded.append(line)
        expanded.append(line)
    return expanded

def expand_universe_vertical(matrix):
    matrix = transpose_matrix(matrix)
    matrix = expand_universe_horizontal(matrix)
    return transpose_matrix(matrix)


def expand_universe(matrix):
    return expand_universe_vertical(expand_universe_horizontal(matrix))


def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


def solve_a():
    expanded = expand_universe(puzzle)
    star_dict = defaultdict()
    for y in range(len(expanded)):
        for x in range(len(expanded[0])):
            if expanded[y][x] != 0:
                star_dict[expanded[y][x]] = (x,y)

    sum_up = 0
    for i in range(1, len(star_dict)+1):
        for j in range(i, len(star_dict)+1):
            sum_up += get_distance(star_dict[i], star_dict[j])

    return sum_up


def solve_b():
    # code goes here
    return 0

#  ----------   Start   ----------   #

puzzle = prepare_input()

run_puzzles(day, year, solve_a, solve_b)
