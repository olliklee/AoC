# # #  Solutions of Advent of Code
# # #  Oliver Kleemann
from aoc_helper import *
import re
from math import prod

year, day = "2025", "06"


def calc_part1(formulars) -> int:
    result = 0
    for term in formulars:
        operator = term[0]
        operands = list(map(int, term[1:]))
        result += sum(operands) if operator == '+' else prod(operands)

    return result


def calc_part2(puzzle: list[str]) -> int:
    result = 0
    length_row = max([len(row) for row in puzzle])

    # alle zeilen auf gleiche länge
    for i in range(len(puzzle)):
        line = puzzle[i] + "   "
        puzzle[i] = line[:length_row]

    # spaltenweise lesen
    output = ''
    for i in range(length_row - 1, -1, -1):
        for line in puzzle:
            char = line[i]
            output += char if char != ' ' else ''
        output += '\n'

    # berechnen
    formulars = output.split('\n\n')
    for formular in formulars:
        formular = formular.strip()
        operator = formular[-1]
        numbers = list(map(int, formular[:-1].split('\n')))
        result += prod(numbers) if operator == '*' else sum(numbers)

    return result


def solve():
    testinput = False

    puzzle = load_input(test=testinput, split_by_line=True)
    rows = [re.findall(r'\w+|\*|\+', line) for line in puzzle]

    formulars = []
    for col in range(len(rows[0])):
        operator = rows[len(puzzle) - 1][col]
        term = [operator]
        for row_number in range(len(puzzle) - 1):
            term.append(int(rows[row_number][col]))
        formulars.append(term)

    part1 = calc_part1(formulars)
    part2 = calc_part2(puzzle)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
