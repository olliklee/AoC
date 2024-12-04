# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

from math import prod

year, day = "2023", "03"


def is_sign(char):
    return not (char.isalnum() or char in ('.', ''))


def is_valid_pos(x, y):
    return 0 <= x < size_x and 0 <= y < size_y


def get_adjacents(x, y):
    possible_adj = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                    (x, y - 1), (x, y + 1),
                    (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
    return [(x, y) for x, y in possible_adj if is_valid_pos(x, y)]


def get_number_start(x, y):
    while x > 0 and puzzle[y][x - 1].isdigit():
        x -= 1

    return x, y


def get_int_at(x, y):
    result = ''
    while puzzle[y][x].isdigit():
        result += puzzle[y][x]
        x += 1
        if x > size_x - 1:
            break

    return int(result)


def solve_a():
    start_num_set = set()
    # Alle 'Zeichen' in der puzzle Matrix finden
    signs = [(y, x) for y in range(size_y) for x in range(size_x) if is_sign(puzzle[y][x])]

    # Gehe alle gefundenen Zeichen durch und speichere die Startkoordinaten
    # jeder einzelnen Zahl in einem Set
    for sign in signs:
        adj = get_adjacents(*sign)
        for y, x in adj:
            if puzzle[y][x].isdigit():
                start_num_set.add(get_number_start(x, y))

    # Suche die zugehörige Zahl der gefundenen Startkoordinaten
    # und addiere sie
    result = 0
    for cood in start_num_set:
        result += get_int_at(*cood)

    return result


def solve_b():
    # Alle Asterisks in der Puzzle Matrix finden
    gears = [(y, x) for y in range(size_y) for x in range(size_x) if puzzle[y][x] == '*']
    # Gehe alle gefundenen Zeichen durch und speichere die Startkoordinaten
    # jeder einzelnen Zahl in einem Set
    result = 0
    for gear in gears:
        adj = get_adjacents(*gear)
        adj_nums_set = set()
        for y, x in adj:
            if puzzle[y][x].isdigit():
                adj_nums_set.add(get_number_start(x, y))
        # Ist es ein Gear mit genau zwei Nachbarn?
        if len(adj_nums_set) == 2:
            result += prod([get_int_at(*cood) for cood in adj_nums_set])

    return result


puzzle = load_input().split('\n')
size_x, size_y = len(puzzle[0]), len(puzzle)

run_puzzles(day, year, solve_a, solve_b)
