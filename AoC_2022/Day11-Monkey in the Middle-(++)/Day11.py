# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict
from math import prod
import re

year, day = "2022", "11"


def prepare_input(puzzle):
    monkey_dict = {}
    for monkey in puzzle:
        split_monkey = [line.split(': ') for line in monkey.split('\n')]

        m_nr = int(split_monkey[0][0].split()[1][:-1])
        st_items = list(map(int,split_monkey[1][1].split(', ')))
        operator = split_monkey[2][1].split()[3] if split_monkey[2][1].split()[4] != 'old' else '**'
        operand = int(split_monkey[2][1].split()[4] if split_monkey[2][1].split()[4] != 'old' else '2')
        test = int(split_monkey[3][1].split()[2])
        true = int(split_monkey[4][1].split('monkey ')[1])
        false = int(split_monkey[5][1].split('monkey ')[1])
        monkey_dict[m_nr] = [st_items, operator, operand, test, true, false]
        
    return monkey_dict


def get_worry_level(old, op, num):
    match op:
        case "+": return old + num
        case "*": return old * num
        case "**": return old ** num
        case _: raise ValueError("Invalid operation")
    

def turn(monkey_dict, monkey_num, kgv, divide = True):
    inspects = 0
    while len(monkey_dict[monkey_num][0]) > 0:
        this_item = monkey_dict[monkey_num][0].pop(0)
        worry = get_worry_level(this_item,
                                monkey_dict[monkey_num][1],
                                monkey_dict[monkey_num][2])
        worry = worry // (3 if divide else 1)
        if not divide:
            worry %= kgv  # keep number small
        
        if worry % monkey_dict[monkey_num][3] == 0:
            throw_to = monkey_dict[monkey_num][4]
        else:
            throw_to = monkey_dict[monkey_num][5]
            
        monkey_dict[throw_to][0].append(worry)
        inspects += 1
    
    return inspects


def process_turns(puzzle, turns, divide=True):
    inspects = defaultdict(int)
    monkey_dict = prepare_input(puzzle)
    kgv =  prod([val[3] for val in monkey_dict.values()])

    for _ in range(turns):
        for monkey_nr in monkey_dict.keys():
            inspects[monkey_nr] += turn(monkey_dict, monkey_nr, kgv, divide=divide)
    return prod(sorted(inspects.values(), reverse=True)[:2])


def solve():
    puzzle = load_input(test=False, delimiter='\n\n')

    part1 = process_turns(puzzle, 20)
    part2 = process_turns(puzzle, 10000, divide=False)
 
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
