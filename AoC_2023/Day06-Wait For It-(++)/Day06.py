# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

import re

year, day = "2023", "06"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final


def prepare_input():
    with open(filename) as f:
        content = [list(map(int, re.findall("\d+", line))) for line in f.read().split("\n")]
    return content


def distance(push, time):
    return (time - push) * push


def solve_a():
    times, dists = puzzle[0], puzzle[1]
    product = 1
    for i, time in enumerate(times):
        result = [distance(push, times[i]) for push in range(1, time - 1) if distance(push, times[i]) > dists[i]]
        product *= len(result)

    return product

def solve_b():
    time = int("".join(map(str, puzzle[0])))
    dist = int("".join(map(str, puzzle[1])))
    result = 0
    for push in range(time // 2, 14, -1):
        if distance(push, time) > dist:
            result += 1
        else:
            break
    for push in range(time // 2 + 1, dist - 14):
        if distance(push, time) > dist:
            result += 1
        else:
            break

    return result

# Slower variant
# def solve_b():
#     time = int("".join(map(str, puzzle[0])))
#     dist = int("".join(map(str, puzzle[1])))
#     result = [distance(push, time) for push in range(14, time - 14) if distance(push, time) > dist]
#
#     return len(result)


### ----------- Start ------------- ###

puzzle = prepare_input()

run_puzzles(day, year, solve_a, solve_b)
