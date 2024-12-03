# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2021", "02"

def solve():
    lines = load_input().split('\n')

    direction = []
    amount = []
    horizontal = depth_a = depth_b = 0
    aim = 0

    for line in lines:
        data = line.split(' ')
        direction.append(data[0])
        amount.append(int(data[1]))

    for i in range(len(direction)):
        if direction[i] == "forward":
            horizontal += amount[i]
            depth_b += amount[i] * aim
        elif direction[i] == "down":
            depth_a += amount[i]
            aim += amount[i]
        else:
            depth_a -= amount[i]
            aim -= amount[i]

    result_a = horizontal * depth_a
    result_b = horizontal * depth_b

    return result_a, result_b

run_puzzle(year, day, solve)