# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2016", "16"


def flip(bin_text, reverse=False):
    flipped = ''.join(['0' if bit == '1' else '1' for bit in bin_text])
    return flipped[::-1] if reverse else flipped


def expand(bin_text):
    return bin_text + '0' + flip(bin_text, reverse=True)


def checksum(bin_text):
    if len(bin_text) % 2 != 0:
        return bin_text
    
    new_checksum = ''.join(['0' if pair[0] != pair[1] else '1'
                            for pair in zip(bin_text[::2], bin_text[1::2])])
    return checksum(new_checksum)


def process(puzzle, max_length):
    binary = puzzle
    while len(binary) < max_length:
        binary = expand(binary)
    password = binary[:max_length]
    return checksum(password)


def solve():
    puzzle = '10010000000110000'
    max_length1 = 272
    max_length2 = 35651584
    
    part1 = process(puzzle, max_length1)
    part2 = process(puzzle, max_length2)
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
