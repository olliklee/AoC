# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict

year, day = '2024', '24'


def calc(op1: int, operator: str, op2: int):
    if operator == 'AND':
        return op1 & op2
    elif operator == 'OR':
        return op1 | op2
    elif operator == 'XOR':
        return op1 ^ op2
    else:
        raise ValueError


def read_program(gates):
    program = defaultdict(tuple)
    for line in gates.split('\n'):
        op1, operator, op2, _, res = line.split()
        program[res] = (op1, operator, op2)
    return program


def solve():
    part2 = 0
    initial, gates = load_input(test=False, delimiter='\n\n')

    register = {k: int(v) for line in initial.split('\n') for k, v in [line.split(': ')]}
    program = read_program(gates)
    while program:
        for k, v in program.items():
            op1, operator, op2 = v
            if op1 in register and op2 in register:
                register[k] = calc(register[op1], operator, register[op2])
                program.pop(k)
                break

    z_regs = sorted([key for key in register.keys() if key.startswith('z')], reverse=True)
    part1 = int(''.join([str(register[v]) for v in z_regs]), 2)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
