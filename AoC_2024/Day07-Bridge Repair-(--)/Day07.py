# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re
from itertools import product

year, day = "2024", "07"


def get_calibration(eq, ops, operators):
    combis = list(product(operators, repeat=len(ops) - 1))
    for combi in combis:
        result = ops[0]
        for i, symbol in enumerate(combi):
            if symbol == '*':
                result *= ops[i + 1]
            elif symbol == '+':
                result += ops[i + 1]
            else:
                result = int(str(result) + str(ops[i + 1]))

            if result > eq:
                break
        if result == eq:
            return result

    return 0  # no combination found


def solve():
    content = load_input(test=False)

    pattern = r'(\d+): ([\d\s]+)$'
    matches = re.findall(pattern, content, re.MULTILINE)
    puzzle = [[int(line[0]), list(map(int, line[1].split()))] for line in matches]

    part1 = 0

    puzzle2 = []
    operators = '*+'
    for eq, operands in puzzle:
        result = get_calibration(eq, operands, operators)
        part1 += result
        if result == 0: puzzle2.append([eq, operands])

    part2 = part1
    operators = '*|+'
    for eq, operands in puzzle2:
        part2 += get_calibration(eq, operands, operators)

    return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
