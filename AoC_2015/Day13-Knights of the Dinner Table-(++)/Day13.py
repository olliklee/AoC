# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re
from itertools import permutations

year, day = "2015", "13"


def calc_happiness(persons, happy_dict):
    seating_plans = permutations(persons)
    persons_count = len(persons)
    max_happiness = 0
    for seat_order in seating_plans:
        seat_order = list(seat_order)
        happiness = 0
        for i in range(persons_count):
            happiness += happy_dict[(seat_order[i], seat_order[(i + 1) % persons_count])]
            happiness += happy_dict[(seat_order[i], seat_order[(i - 1) % persons_count])]
        if happiness > max_happiness:
            max_happiness = happiness
    return max_happiness


def solve():
    puzzle = (load_input()
              .replace("gain ", '')
              .replace('lose ', '-'))

    happy_dict = {
        (p1, p2): int(val)
        for p1, val, p2 in re.findall(r"^(.+) .+ (-?\d+).+ (.+).$", puzzle, re.MULTILINE)
    }
    persons = set([p1 for p1, _ in happy_dict.keys()])

    part1 = calc_happiness(persons, happy_dict)

    for person in persons:
        happy_dict[('Me', person)] = 0
        happy_dict[(person, 'Me')] = 0
    persons.add('Me')

    part2 = calc_happiness(persons, happy_dict)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
