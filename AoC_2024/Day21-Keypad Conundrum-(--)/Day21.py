# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from itertools import permutations

year, day = '2024', '21'

num_pad = {'7': (0, 0), '8': (1, 0), '9': (2, 0),
           '4': (0, 1), '5': (1, 1), '6': (2, 1),
           '1': (0, 2), '2': (1, 2), '3': (2, 2),
           '0': (1, 3), 'A': (2, 3)}

dir_pad = {'^': (1, 0), 'A': (2, 0),
           '<': (0, 1), 'v': (1, 1), '>': (2, 1)}


def go_to_button(pad, start, button):
    return convert_to_direction(pad, start, button)


def convert_to_direction(pad, start, end):
    sx, sy = pad[start]
    ex, ey = pad[end]
    dx, dy = abs(sx - ex), abs(sy - ey)
    hor = dx * '<' if sx > ex else dx * '>'
    ver = dy * '^' if sy > ey else dy * 'v'
    return set(permutations(hor + ver))


def convert_to_route_string(pad, route, min_len):
    i = 0
    r = route[i]
    full_route = go_to_button(pad, 'A', r) + 'A'
    for i in range(len(route) - 1):
        next_route = go_to_button(pad, route[i], route[i + 1]) + 'A'
        if len(next_route) == 1:
            full_route += next_route
        
    return full_route


def solve():
    part1 = part2 = 0
    puzzle = load_input(test=True, split_by_line=True)
    
    print(go_to_button(num_pad, 'A', '1'))
    
    # for row in puzzle:
    #     print(convert_to_route_string(num_pad, row))
    #     robot1 = min([robot for robot in convert_to_route_string(num_pad, row)], key=len)
    #     print(robot1)
    #     robot2 = min([robot for robot in convert_to_route_string(dir_pad, robot1)], key=len)
    #     robot3 = min([robot for robot in convert_to_route_string(dir_pad, robot2)], key=len)
    #
    #     print(row, int(row[:-1]), len(robot3), robot3)
    #     part1 += int(row[:-1]) * len(robot3)
    # if row == '379A':
    #     print(robot1)
    #     print(robot2)
    #     print(robot3)


    return part1, part2

run_puzzle(year, day, solve)

# 196304 too high

# ^A^^<<A>>AvvvA
# <A>A<AAv<AA>>^AvAA^Av<AAA^>A
# <v<A>>^AvA^A <vA <AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# v<<A>>^AvA^A v<<A>>^AAv<A<A>>^AAvAA^<A>Av<A^>AA<A>Av<A<A>>^AAA<Av>A^A
