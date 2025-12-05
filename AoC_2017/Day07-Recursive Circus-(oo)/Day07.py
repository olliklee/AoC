# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict
import re

year, day = "2017", "07"


def solve():
    puzzle = load_input(test=True, split_by_line=True)
    
    # create dict
    node_dict = defaultdict(list)
    for line in puzzle:
        name, weight, node_lst = re.match(r"(\w+) \((\d+)\)(?: -> (.*))?", line).groups()
        node_dict[name].append(int(weight))
        if node_lst:
            node_dict[name].append(node_lst.split(', '))
    
    fathers = defaultdict(list)
    for k, v in node_dict.items():
        if len(v) == 1:
            print(k, 'no ancestors')
    
    part1 = 0
    part2 = 0

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
