# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2016", "07"


def is_abba(seq):
    if seq[0] == seq[3] and seq[1] == seq[2] and seq[0] != seq[1] :
        return True
    return False


def check_for_abba(text):
    return any(is_abba(text[i:i+4]) for i in range(len(text) - 3))


def is_aba(seq):
    return seq[0] == seq[2] and seq[0] != seq[1]


def collect_aba (text):
    return [text[i:i+3] for i in range(len(text) - 2) if is_aba(text[i:i+3])]

def solve():
    puzzle = load_input(test=True, split_by_line=True)
    part1 = part2 = 0
    for line in puzzle:
        parts = re.split(r'(\[.*?\])', line)
        valid_outside = any(check_for_abba(part) for part in parts if not part.startswith('['))
        valid_inside = not any(check_for_abba(part[1:-1]) for part in parts if part.startswith('['))
        if valid_outside and valid_inside:
            part1 += 1

    for line in puzzle:
        parts = re.split(r'(\[.*?\])', line)
        abas_inside = collect_aba(parts)
        print(list(abas_inside))


    part2 = 0

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
