# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re
from collections import defaultdict

year, day = "2017", "08"


def is_valid(registers, reg, comp, num):
    r, n = registers[reg], int(num)
    match comp:
        case '<': return r < n
        case '>': return r > n
        case '<=': return r <= n
        case '>=': return r >= n
        case '==': return r == n
        case '!=': return r != n
        case _: raise Exception("Invalid register")
    
    # return eval(f'{r} {comp} {n}')   -> about 300 % slower

def solve():
    puzzle = load_input()
    program = re.findall(r'(.+) (inc|dec) (-?\d+) if (.+) (<|>|<=|>=|!=|==) (-?\d+)',
                           puzzle,
                           re.MULTILINE)
    
    highest_value = 0
    registers = defaultdict(int)
    
    for instruction in program:
        register, op, value, reg, comp, num = instruction
        if op == 'inc':
            registers[register] += int(value) * is_valid(registers, reg, comp, num)
        elif op == 'dec':
            registers[register] -= int(value) * is_valid(registers, reg, comp, num)
        else:
            raise Exception("Invalid operator")
        
        if registers[register] > highest_value:
            highest_value = registers[register]
            
    part1 = max(registers.values())
    part2 = highest_value

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
