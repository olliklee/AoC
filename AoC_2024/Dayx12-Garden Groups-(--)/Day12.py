# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2024", "12"

def get_neighbours(pos):
    x, y = pos
    return [(x+1, y), (x-1, y), (x, y+1), (x,y-1)]

def get_plant(puzzle, position):
    return puzzle[(position[1], position[0])]

def get_area(puzzle, pos, plant, inside):
    if pos not in puzzle:
        return

    p = get_plant(puzzle, pos)
    if p != plant or pos in inside:
        return

    inside.append(pos)

    for n in get_neighbours(pos):
        get_area(puzzle, n, p, inside)

def count_walls(area):
    wall_count = 0
    for pos in area:
        walls = set()
        for n in get_neighbours(pos):
            if n not in area:
                walls.add(n)
        wall_count += len(walls)
    return wall_count


def solve():
    puzzle = load_input(test=True, split_by_line=True)
    garden = {(x,y): puzzle[x][y] for y in range(len(puzzle[0])) for x in range(len(puzzle))}
    plants = {garden[pos] for pos in garden}

    part1 = part2 = 0

    for plant in plants:
        area = []
        first_pos = ()
        for pos in garden:
            if get_plant(garden, pos) == plant:
                first_pos = pos
                break

        get_area(garden, first_pos, plant, area)

        size = len(area)
        walls = count_walls(area)

        print(plant, size, walls)

        part1 += size * walls

    return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)