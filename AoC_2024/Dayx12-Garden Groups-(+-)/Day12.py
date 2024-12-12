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
    if pos not in puzzle: return

    p = get_plant(puzzle, pos)
    if p != plant or pos in inside: return

    inside.append(pos)

    for n in get_neighbours(pos):
        get_area(puzzle, n, p, inside)

def get_walls(area):
    # wall_count = 0
    walls = []
    for pos in area:
        # walls.clear()
        for n in get_neighbours(pos):
            if n not in area:
                walls.append(n)
        # wall_count += len(walls)


    return len(walls), walls

def sort_connected_fields(walls):
    if not walls:
        return []

    # Wandle die Liste in ein Set für schnelleren Zugriff
    fields_set = set(walls)
    sorted_fields = []

    # Wähle den Startpunkt (kleinste x, y)
    pos = min(walls)
    sorted_fields.append(pos)

    fields_set.remove(pos)

    # Iterativ die Nachbarn finden
    while fields_set:
        x, y = pos
        # Potenzielle Nachbarn berechnen
        neighbours = [
            (x+1, y),  # rechts
            (x-1, y),  # links
            (x, y+1),  # oben
            (x, y-1)   # unten
        ]
        # Nachbarn durchsuchen, die noch in `fields_set` sind
        for n in neighbours:
            if n in fields_set:
                pos = n
                sorted_fields.append(pos)
                fields_set.remove(pos)
                break

    return sorted_fields


def solve():
    puzzle = load_input(test=True, split_by_line=True)
    garden = {(x,y): puzzle[x][y] for y in range(len(puzzle[0])) for x in range(len(puzzle))}
    plants = {garden[pos] for pos in garden}

    part1 = part2 = 0

    visited = set()
    for pos in garden:
        if pos in visited: continue

        area = []
        plant = get_plant(garden, pos)
        get_area(garden, pos, plant, area)
        visited.update(area)

        size = len(area)
        walls_count, walls = get_walls(area)
        print(plant, calc_discount(walls))
        part1 += size * walls_count

    return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)