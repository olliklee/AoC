# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2016", "20"


def optimize_interval(puzzle):
    puzzle.sort()
    result = []
    for start, end in puzzle:
        if not result or result[-1][1] < start - 1:  # not overlap
            result.append((start, end))
        else:  # overlap
            result[-1] = (result[-1][0], max(result[-1][1], end))
    
    return result


def solve():
    puzzle = load_input()
    puzzle = [(int(a), int(b)) for a, b in re.findall(r"(\d+)-(\d+)", puzzle, re.MULTILINE)]
    
    intervals = optimize_interval(puzzle)
    part1 = intervals[0][1] + 1
    part2 = sum([intervals[i + 1][0] - intervals[i][1] - 1 for i in range(len(intervals) - 1)])
    # part2 = len(intervals) - 1 # works only, if the gap between the intervals is always one
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
