# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import load_input, run_puzzle, text_to_dictmap

year, day = "2025", "04"

directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]


def count_neighbours(locations, position:tuple[int,int]) -> int:
    x, y = position
    return sum([(x + dx, y + dy) in locations for dx, dy in directions])


def count_removables(locations) -> int:
    return sum([count_neighbours(locations, position) < 4 for position in locations])


def remove_removables(locations):
    removed_positions = set()
    for position in locations:
        if count_neighbours(locations, position) < 4:
            removed_positions.add(position)

    locations.difference_update(removed_positions)


def solve():
    puzzle = load_input(test=False)
    matrix = text_to_dictmap(puzzle)
    locations = set((k for k, v in matrix.items() if v == "@"))

    part1 = count_removables(locations)

    part2 = len(locations) # startwert ist anzahl der rollen zu beginn
    while True:
        before = len(locations)
        remove_removables(locations)
        if len(locations) == before:
            break

    part2 -= len(locations)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
