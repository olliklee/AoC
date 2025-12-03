# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2025", "03"


def get_jolt(digit_list: list[int], digits: int, result: str = ''):
    length = len(digit_list)

    if digits == 0 or not digit_list:
        return int(result)

    new_digit_list = digit_list[:length - digits + 1]
    highest = max(new_digit_list)

    while True:
        position = new_digit_list.index(highest)
        if position <= (length - digits):
            break
        highest -= 1

    new_digit_list = digit_list[position + 1:]
    new_result = result + str(highest)

    return get_jolt(new_digit_list, digits - 1, new_result)


def solve():
    part1 = part2 = 0
    puzzle = load_input(test=False, split_by_line=True)

    for row in puzzle:
        digit_list = list(map(int, list(row)))
        part1 += get_jolt(digit_list, 2)
        part2 += get_jolt(digit_list, 12)

    return part1, part2

#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
