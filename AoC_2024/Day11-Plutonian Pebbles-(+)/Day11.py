# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2024", "11"


def split_into_two(num):
    new = str(num)
    l = new[:len(new) // 2]
    r = new[len(new) // 2:]
    return int(l), int(r)


def solve():
    part1 = part2 = 0
    final = True  # false for test input
    puzzle = '3 386358 86195 85 1267 3752457 0 741' if final else '125 17'
    
    puzzle = list(map(int, puzzle.split()))
    
    for _ in range(25):
        new_puzz = []
        for num in puzzle:
            if num == 0:
                new_puzz.append(1)
            elif len(str(num)) % 2 == 0:
                new_puzz.extend(split_into_two(num))
            else:
                new_puzz.append(num * 2024)
            
            puzzle = new_puzz[:]
        
        part1 = len(puzzle)
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)