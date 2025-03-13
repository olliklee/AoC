#  Solutions of Advent of Code
#  Oliver Kleemann

from aoc_helper import *

year, day = "2022", "03"


def solve():
    rucksacks = load_input(split_by_line=True)
    
    score = 0
    # split bags in 2 compartments and find the common item
    for bag in rucksacks:
        compartment1 = set(bag[:len(bag) // 2])
        compartment2 = set(bag[len(bag) // 2:])
        in_both = list(compartment1.intersection(compartment2))[0]
        score += (ord(in_both) - 96) + (58 if in_both.isupper() else 0)  # calculation with ascii
    
    part1 = score
    
    score = 0
    teams = [(set(rucksacks[i]), set(rucksacks[i + 1]), set(rucksacks[i + 2])) for i in range(0, len(rucksacks) - 1, 3)]
    
    # find the badge of each team
    for team in teams:
        a, b, c = team
        badge = list(a.intersection(b.intersection(c)))[0]
        score += (ord(badge) - 96) + (58 if badge.isupper() else 0)  # calculation with ascii
    
    part2 = score
    
    return part1, part2


run_puzzle(day, year, solve)
