# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2015", "08"


def solve():
    puzzle = load_input(split_by_line=True)
    length_of_lines = [len(a) for a in puzzle]
    len_of_unescaped_list = []

    for item in puzzle:
        item = list(item.strip('"'))
        if item[-1] == '\\':  # sonderfall letztes Element ein backlash
            item[-1] = "a"    # backlashdurch beliebiges Zeichen ersetzen
        item = "".join(item)
        len_of_unescaped_list.append(len(bytes(item, 'utf-8').decode('unicode_escape')))

    part1 = sum(length_of_lines) - sum(len_of_unescaped_list)

    len_of_escaped_list = []
    for item in puzzle:
        sum_of_additional_chars = item.count('\\') + item.count('"') + 2
        len_of_escaped_list.append(len(item) + sum_of_additional_chars)

    part2 = sum(len_of_escaped_list) - sum(length_of_lines)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
