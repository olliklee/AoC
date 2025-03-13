# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict

year, day = "2016", "12"

def run_program(program, registers):
    pointer = 0
    while pointer < len(program):
        pointer = handle_instruction(program, registers, pointer)
    
    return registers['a']

def handle_instruction(program, registers, pointer):
    command, params = program[pointer]
    
    match command:
        case "cpy":
            registers[params[1]] = int(params[0]) if params[0].isnumeric() else registers[params[0]]
        case "inc":
            registers[params[0]] += 1
        case "dec":
            registers[params[0]] -= 1
        case "jnz":
            value = int(params[0]) if params[0].isnumeric() else registers[params[0]]
            if value != 0:
                return pointer + int(params[1])
    
    return pointer + 1
    
def solve():
    puzzle = load_input(test=False, split_by_line=True)
    
    program = defaultdict(list)
    registers = defaultdict(int)

    # init program
    for i, line in enumerate(puzzle):
        line = line.split(' ')
        program[i] = [line[0], line[1:]]
    program = dict(program)
     
    part1 = run_program(program, registers)
    
    registers.clear()
    registers['c'] = 1
    part2 = run_program(program, registers)
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
