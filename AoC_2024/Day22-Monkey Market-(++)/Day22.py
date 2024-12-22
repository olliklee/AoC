# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict

year, day = '2024', '22'

seq_dict = defaultdict(list)


def prumi(l, r):
    return (l ^ r) % 16777216


def next_number(num, steps):
    result = num
    last_digits = []
    for _ in range(steps):
        result = prumi(result * 64, result)
        result = prumi(result // 32, result)
        result = prumi(result * 2048, result)
        last_digits.append(result % 10)

    add_sequences(num, last_digits)
    return result


def add_sequences(num, digits):
    digits.insert(0, num % 10)
    local_dict = defaultdict(int)
    for i in range(len(digits) - 4):
        seq = (digits[i] - digits[i + 1],
               digits[i + 1] - digits[i + 2],
               digits[i + 2] - digits[i + 3],
               digits[i + 3] - digits[i + 4])

        if seq not in local_dict.keys():
            local_dict[seq] = digits[i + 4]

    for seq in local_dict.keys():
        if seq not in seq_dict.keys():
            seq_dict[seq] = [local_dict[seq]]
        else:
            seq_dict[seq].append(local_dict[seq])


def solve():
    part1 = part2 = 0

    puzzle = load_input(test=False, split_by_line=True)
    secrets = list(map(int, puzzle))

    all_results = [next_number(i, 2000) for i in secrets]

    bananas = 0
    for seq in seq_dict.values():
        bananas = max(bananas, sum(seq))

    part1 = sum(all_results)
    part2 = bananas

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
