# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2015", "11"

VALID_LETTERS = set('abcdefghjkmnpqrstuvwxyz')


def is_valid(word):
    if not set(word).issubset(VALID_LETTERS):
        return False

    if not any(ord(word[i]) + 1 == ord(word[i + 1]) \
               and ord(word[i]) + 2 == ord(word[i + 2])\
               for i in range(len(word) - 2)):
        return False

    pairs = 0
    i = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            pairs += 1
            i += 1
        if pairs >= 2:
            return True
        i += 1

    return False


def increment_string(word: str) -> str:
    word = list(word)
    for i in range(len(word) - 1, -1, -1):
        if word[i] == 'z':
            word[i] = 'a'
        else:
            word[i] = chr(ord(word[i]) + 1)
            break
    return ''.join(word)


def solve():
    last_pw = 'cqjxjnds'
    pw = last_pw
    next_pws = []
    while len(next_pws) < 2:
        pw = increment_string(pw)
        if is_valid(pw):
            next_pws.append(pw)

    part1 = next_pws[0]
    part2 = next_pws[1]

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
