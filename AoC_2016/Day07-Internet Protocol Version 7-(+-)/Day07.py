# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2016", "07"


def get_parts(text):
    return re.split(r'(\[.*?\])', text)


def is_abba(seq):
    if seq[0] == seq[3] and seq[1] == seq[2] and seq[0] != seq[1] :
        return True
    return False


def is_aba(seq: str) -> (str | None):
    return seq if seq[0] == seq[2] and seq[0] != seq[1] else None


def check_for_abba(text: str) -> bool:
    return any(is_abba(text[i:i+4]) for i in range(len(text) - 3))


def collect_aba (text: str) -> list[str]:
    return [text[i:i+3] for i in range(len(text) - 2) if is_aba(text[i:i+3])]


def solve():
    puzzle = load_input(test=False, split_by_line=True)
    part1 = part2 = 0
    for line in puzzle:
        parts = get_parts(line)
        valid_outside = any(check_for_abba(part) for part in parts if not part.startswith('['))
        valid_inside = not any(check_for_abba(part[1:-1]) for part in parts if part.startswith('['))
        if valid_outside and valid_inside:
            part1 += 1

    puzzle = ['aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke', 'zazbz[bzb]cdb']
    for line in puzzle:
        parts = get_parts(line)
        abas_inside, abas_outside = None, None

        for part in parts:
            if part.startswith('['):
                abas_inside = collect_aba(part)
            else:
                abas_outside = collect_aba(part)


    part2 = 0

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
