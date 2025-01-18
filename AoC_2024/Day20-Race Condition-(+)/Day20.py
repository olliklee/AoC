# # #  Solutions of Advent of Code
# # #  Oliver Kleemann


from collections import defaultdict

from aoc_helper import *

year, day = '2024', '20'


def get_start_and_finish(maze):
    start = finish = None
    for pos, spot in maze.items():
        if spot == 'E':
            finish = pos
        if spot == 'S':
            start = pos
        if start and finish:
            break

    return start, finish


def numerize(maze, start, finish):
    pos = start
    counter = 1
    while pos != finish:
        maze[pos] = counter
        x, y = pos
        neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for n in neighbours:
            if maze[n] == '.':
                pos = n
                counter += 1
                break
            elif n == finish:
                maze[n] = counter + 1
                return


def get_shortcuts(maze):
    short_cuts = defaultdict(list)
    wall = '#'
    for pos, spot in maze.items():
        x, y = pos
        if spot != '#':
            continue

        hl, hr = maze.get((x - 1, y), None), maze.get((x + 1, y), None)
        vo, vu = maze.get((x, y - 1), None), maze.get((x, y + 1), None)
        if hl != wall and hr != wall and hl and hr:
            delta = abs(hl - hr)
        elif vo != wall and vu != wall and vo and vu:
            delta = abs(vo - vu)
        else:
            continue
        short_cuts[delta-2].append((x, y))

    return short_cuts


def solve():
    part1 = part2 = 0

    puzzle = load_input(test=False)
    maze = text_to_dictmap(puzzle)

    start, finish = get_start_and_finish(maze)
    numerize(maze, start, finish)
    shorts = get_shortcuts(maze)
    for shortcut in shorts:
        if shortcut >= 100:
            part1 += len(shorts[shortcut])

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
