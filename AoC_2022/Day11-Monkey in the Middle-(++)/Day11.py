# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict
from math import prod
import re

year, day = "2022", "11"


def prepare_input(puzzle):
    # monkey_number: [[items], (operator, operand), test, true_monkey, false_monkey]
    monkey_dict = {}
    for monkey in puzzle:
        lines = monkey.split('\n')
        result = []
        for i, line in enumerate(lines):
            match i:
                case 0 | 3 | 4 | 5: result.append(int(re.findall(r'\d+', line)[0]))
                case 1: result.append(list(map(int, re.findall(r'(\d+)', line))))
                case 2: result.extend(re.findall(r'.*(.+) (old|\d+)', line))
        monkey_dict[result[0]] = result[1:]
    return monkey_dict


def get_worry_level(old, operation):
    op, num = operation
    match op:
        case "+": return old + int(num)
        case "*": return old * (int(num) if not num == 'old' else old)
        case _: raise ValueError("Invalid operation")
    

def turn(monkey_dict, monkey_num, kgv, divide = True):
    inspects = 0
    while len(monkey_dict[monkey_num][0]) > 0:
        this_item = monkey_dict[monkey_num][0].pop(0)
        worry = get_worry_level(this_item, monkey_dict[monkey_num][1])
        worry = worry // (3 if divide else 1)
        if not divide:
            worry %= kgv  # keep number small
        
        if worry % monkey_dict[monkey_num][2] == 0:
            throw_to = monkey_dict[monkey_num][3]
        else:
            throw_to = monkey_dict[monkey_num][4]
            
        monkey_dict[throw_to][0].append(worry)
        inspects += 1
    
    return inspects


def process_turns(puzzle, turns, divide=True):
    inspects = defaultdict(int)
    monkey_dict = prepare_input(puzzle)
    kgv =  prod([val[2] for val in monkey_dict.values()])

    for _ in range(turns):
        for monkey_nr in monkey_dict.keys():
            inspects[monkey_nr] += turn(monkey_dict, monkey_nr, kgv, divide=divide)
    return prod(sorted(inspects.values(), reverse=True)[:2])


def solve():
    puzzle = load_input(delimiter='\n\n')

    part1 = process_turns(puzzle, 20)
    part2 = process_turns(puzzle, 10000, divide=False)
 
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
