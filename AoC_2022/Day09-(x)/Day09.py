# # #  Solutions of Advent of Code
# # #  Oliver Kleemann
# # #  inspired by gravitar

from aoc_helper import *
from pygame import Vector2 as V2

year, day = '2022', '09'


def read_puzzle(file):
    with open(file) as f:
        return [line.strip().split() for line in f.readlines()]


def move(rope):
    for i in range(len(rope) - 1):
        s1, s2 = rope[i], rope[i + 1]
        if s1.distance_to(s2) >= 2:
            dx, dy = s1 - s2
            if abs(dx) > 1:  dx //= abs(dx)
            if abs(dy) > 1:  dy //= abs(dy)
            rope[i + 1] = s2 + V2(dx, dy)
    return rope


def move_all(puzzle, rope_length):
    dir_dict = dict(R=V2(1, 0), L=V2(-1, 0), U=V2(0, -1), D=V2(0, 1))
    
    rope, tail_trail = [V2(0, 0)] * rope_length, set()
    for direction, steps in puzzle:
        for _ in range(int(steps)):
            rope[0] = rope[0] + dir_dict[direction]
            rope = move(rope)
            tail_trail.add(tuple(rope[-1]))
    return len(tail_trail)


def solve():
    puzzle = [line.split() for line in load_input(split_by_line=True)]
    part1 = move_all(puzzle, 2)
    part2 = move_all(puzzle, 10)
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
