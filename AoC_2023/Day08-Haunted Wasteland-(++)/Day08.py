# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

from math import lcm

year, day = "2023", "08"
filename = f"Day{day}_input.txt"


def prepare_input() -> (str, dict):
    with open(filename) as f:
        content = f.read().split("\n")
    return content[0], {k: v.strip('()').split(', ') for k, v in [line.split(' = ') for line in content[2:]]}


def solve_a() -> int:
    pos = 'AAA'  # starting position
    steps = 0
    done = False
    while not done:
        for direction in commands:
            steps += 1
            pos = maps[pos][0] if direction == 'L' else maps[pos][1]

            if pos == 'ZZZ':  ## ending position
                done = True
                break

    return steps


def solve_b() -> int:
    start_list = [mp for mp in maps if mp.endswith('A')]
    positions = start_list
    step_list = []
    steps = 0

    done = False
    while not done:
        for direction in commands:
            steps += 1
            # calculate new positions
            new_pos = [maps[pos][0] if direction == 'L' else maps[pos][1] for pos in positions]
            positions = new_pos
            # if end position reached, add actuals steps to the step_list
            step_list.extend(steps for pos in positions if pos[2] == 'Z')

            # all cycles found?
            if len(step_list) == 6:
                done = True

    return lcm(*step_list) # lowest common multiplicator


#  ----------   Start   ----------   #

commands, maps = prepare_input()
run_puzzles(day, year, solve_a, solve_b)
