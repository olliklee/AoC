# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2015", "17"


def get_containers(containers, amount: int,  filled=None, pointer: int = 0):
    if filled is None:
        filled = []
    if amount == 0:
        return [filled]
    elif pointer >= len(containers):
        return []
    else:
        valid_combinations = []
        while pointer < len(containers) and containers[pointer] <= amount:
            new_filled = filled + [containers[pointer]]
            valid_combinations.extend(get_containers(containers, amount - containers[pointer], new_filled, pointer + 1))
            pointer += 1
        return valid_combinations


def solve():
    puzzle = load_input(split_by_line=True)

    containers = sorted(list(map(int, puzzle)))

    solutions = get_containers(containers, 150)

    shortest = len(sorted(solutions, key=len)[0])
    shortest_count = len(list(filter(lambda x: len(x) == shortest, solutions)))

    part1 = len(solutions)
    part2 = shortest_count

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
