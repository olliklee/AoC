# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from itertools import permutations
from collections import defaultdict

year, day = "2015", "09"


def calculate(locations, routes, min_dist, max_dist):
    possible_routes = permutations(locations)

    for santas_route in possible_routes:
        total_dist = 0
        for i in range(len(locations) - 1):
            total_dist += routes[santas_route[i] + santas_route[i + 1]]

        if total_dist > max_dist:
            max_dist = total_dist

        if total_dist < min_dist:
            min_dist = total_dist
    return min_dist, max_dist


def solve():
    puzzle = load_input(split_by_line=True)
    min_dist, max_dist = 999999, 0
    locations = set()
    routes = defaultdict(int)

    for line in puzzle:
        line = line.split()
        start, _, destination, _, distance = line
        distance = int(distance)

        locations.add(start)
        locations.add(destination)
        routes[start + destination] = int(distance)
        routes[destination + start] = int(distance)

    part1, part2 = calculate(locations, routes, min_dist, max_dist)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
