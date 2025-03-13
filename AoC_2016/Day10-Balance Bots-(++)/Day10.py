# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict
import re
from math import prod

year, day = '2016', '10'


def handle_item(bots, outputs, t, v, n):
    if t == 'output':
        outputs[v] = n
    elif t == 'bot':
        bots[v].append(n)
        if set(bots[v]) == {17, 61}:
            return v


def handle_bots(bots, instructions, outputs, results):
    for bot, vals in bots.items():
        if len(vals) == 2:
            low, high = sorted(vals)
            bots[bot] = []
            lt, lv, ht, hv = instructions[bot]

            res_low = handle_item(bots, outputs, lt, lv, low)
            res_high = handle_item(bots, outputs, ht, hv, high)
            
            if 1 not in results.keys():
                if result := res_low or res_high:
                    results[1] = result
            
            if 2 not in results.keys():
                if all(outputs[i] for i in range(3)):
                    results[2] = prod(outputs[i] for i in range(3))
            
            return


def solve():
    bots = defaultdict(list)
    instructions = defaultdict(list)
    outputs = defaultdict(int)
    results = defaultdict(int)
    
    puzzle = load_input(split_by_line=True)
    
    # prepare dictionaries
    for line in puzzle:
        if line.startswith('value'):
            val, bot = map(int, re.findall(r'(\d+)', line))
            bots[bot].append(val)
            continue
            
        pattern = r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)$'
        match = re.match(pattern, line)
        if match:
            bot, lt, lv, ht, hv = (int(match.group(1)), match.group(2), int(match.group(3)),
                                   match.group(4), int(match.group(5)))
            instructions[bot] = [lt, lv, ht, hv]
    
    # handle bots and instructions
    while not (len(results) == 2):
        handle_bots(bots, instructions, outputs, results)
        
    part1, part2 = results[1], results[2]
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
