# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re
from itertools import takewhile, islice


year, day = '2016', '09'

### my solution for part1 - not working for part 2
def expand(puzzle):
    expanded = []
    while puzzle:
        marker = re.search(r'\((\d+)x(\d+)\)', puzzle)
        if not marker:
            expanded.extend(puzzle)
            break

        start, end, length, times = marker.start(), marker.end(), int(marker.group(1)), int(marker.group(2))
        expanded.extend(puzzle[:start])
        expanded.extend(puzzle[end : end + length] * times)
        puzzle = puzzle[end + length:]
    
    return ''.join(expanded)

### https://www.reddit.com/r/adventofcode/comments/5hbygy/comment/daz5a00/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
### What a wonderful piece of code!
def decompress(data, recurse):
    answer = 0
    chars = iter(data)
    for c in chars:
        if c == '(':
            n, m = map(int, [''.join(takewhile(lambda c: c not in 'x)', chars)) for _ in (0, 1)])
            s = ''.join(islice(chars, n))
            answer += (decompress(s, recurse) if recurse else len(s))*m
        else:
            answer += 1
    return answer


def solve():
    puzzle = load_input()
    
    part1 = decompress(puzzle, False)
    part2 = decompress(puzzle, True)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
