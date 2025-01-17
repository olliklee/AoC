# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2015", "05"


def is_allowed(word):
    return not re.search(r'(ab|cd|pq|xy)', word)


def has_doubles(word):
    return re.search(r'(.)\1', word)


def has_3_vowels(word):
    return len(re.findall(r'[aeiou]', word)) >= 3


def has_xyx(word):
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            return True
    return False


def has_double_pair(word):
    for i in range(len(word) - 1):
        pair = word[i] + word[i + 1]
        if pair in word[i + 2:]:
            return True
    return False


def solve():
    puzzle = load_input(split_by_line=True)

    part1 = sum([1 for w in puzzle if is_allowed(w) and has_doubles(w) and has_3_vowels(w)])
    part2 = sum([1 for w in puzzle if has_double_pair(w) and has_xyx(w)])

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
