# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2025", "02"


def solve():
    puzzle = load_input(test=False, delimiter=",")
    pattern = re.compile(r'^(.+?)\1+$') # repeating patterns

    part1 = part2 = 0

    for ranges in puzzle:
        start_id, stop_id = map(int,ranges.split("-"))
        sequence = range(start_id, stop_id + 1)

        for number in sequence:
            number_str = str(number)
            length = len(number_str)

            # part 1 rule
            half = length // 2
            if length % 2 and number_str[:half] == number_str[half:]:
                part1 += number

            # part 2 rule
            matched = pattern.match(number_str)
            if matched:
                part2 += number

    return part1, part2

#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
