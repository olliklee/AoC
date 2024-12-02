# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2024.aoc_helper import *

year, day = "2024", "02"


def solve():
    result_a, result_b = 0, 0

    for line in puzzle:
        value_list = list(map(int, line.split()))
        list_length = len(value_list)

        diffs = [value_list[i] - value_list[i + 1] for i in range(list_length - 1)]

        zeros = diffs.count(0)
        errors = zeros
        print(diffs)
        diffs = [x for x in diffs if x != 0]
        print(diffs)

        positives = sum(1 for diff in diffs if diff > 0)
        one_direction = positives in [0, len(diffs)]
        valid_direction = positives in [1, len(diffs) - 1]
        invalid_directions = positives not in [0,1, len(diffs), len(diffs) - 1]

        maximum = max(list(map(abs, diffs)))

        errors += valid_direction +\
            2 if invalid_directions else 0 +\
            2 if maximum > 3 else 0

        if errors == 0 and one_direction:
            result_a += 1

        if errors < 2:
            result_b += 1

    return result_a, result_b


### ----------- Start ------------- ###

puzzle = load_input(day, test=False).split('\n')

run_puzzle(day, year, solve)
