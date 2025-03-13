#  Solutions of Advent of Code
#  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2022", "04"


def solve():
    part1 = part2 = 0
    puzzle = load_input()
    sections = [tuple(map(int, match)) for match in re.findall(r'(\d+)-(\d+),(\d+)-(\d+)', puzzle, re.MULTILINE)]
    
    for line in sections:
        from1, to1, from2, to2 = line
        elf1, elf2 = set(range(from1, to1 + 1)), set(range(from2, to2 + 1))
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            part1 += 1
        if len(elf1.intersection(elf2)) > 0:
            part2 += 1
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(year, day, solve)

