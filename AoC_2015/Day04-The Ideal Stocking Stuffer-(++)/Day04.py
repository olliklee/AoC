# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import hashlib

year, day = "2015", "04"


def solve():
    part1 = part2 = 0
    input_data = 'yzbqklnj'

    index = 0
    while not (part1 and part2):
        index += 1
        md5 = hashlib.md5()
        key = input_data + str(index)
        inp_enc = key.encode('utf-8')
        md5.update(inp_enc)
        result = md5.hexdigest()
        if result[0:6] == '000000':
            part2 = index
        if result[0:5] == '00000':
            if not part1:
                part1 = index

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)

# 9962624
