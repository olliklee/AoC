# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2017", "06"


def solve():
    puzzle = list(map(int, load_input(delimiter='\t')))
    seen = {}
    mem_len = len(puzzle)
    redistribution = 0

    while tuple(puzzle) not in seen:
        seen[tuple(puzzle)] = redistribution
        
        max_mem = max(puzzle)
        start_block = puzzle.index(max_mem)
        puzzle[start_block] = 0
        for i in range(1, max_mem + 1):
            puzzle[(start_block + i) % mem_len] += 1
            
        redistribution += 1
        
    part1 = redistribution
    part2 = redistribution - seen[tuple(puzzle)]
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
