# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from hashlib import md5

year, day = "2016", "05"


def solve():
    puzzle = 'uqwqemis'
    # puzzle = 'abc'
    pwd1 = ''
    pwd2 = list('--------')

    idx = 0

    while '-' in pwd2:

        word = puzzle + str(idx)
        hsh = md5(word.encode()).hexdigest()
        if hsh.startswith('00000'):
            pos, val = hsh[5], hsh[6]
            pwd1 += pos

            if pos in list('01234567'):
                if pwd2[int(pos)] == '-':
                    pwd2[int(pos)] = val
                    print(f'\b\b\b{pwd2.count("-")}', end='')

        idx += 1
    part1 = pwd1[:8]
    part2 = ''.join(pwd2)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
