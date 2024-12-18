# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2024", "18"


def solve():
    part1 = part2 = None
    
    test = 0
    puzzle = load_input(test=test)
    dim = range(7) if test == 1 else range(71)
    steps = 11 if test == 1 else 1023
    
    actual_map = {(x, y): '.' for y in dim for x in dim}
    falling_bytes = list(re.findall(r'(\d+),(\d+)',puzzle))
    
    max_byte = len(falling_bytes)
    step = 0
    way = dijkstra_map(actual_map, (0, 0), (dim[-1], dim[-1]))
    while step < max_byte:
        x, y =  tuple(map(int,falling_bytes[step]))
        actual_map[x, y] = '#'
        if (x,y) in way:
            way = dijkstra_map(actual_map, (0, 0), (dim[-1], dim[-1]))
            if not way:
                part2 = f'{x},{y}'
                break
        if step == steps:
            part1 = len(way) - 1
        
        step += 1
      
    return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)

#141 too low