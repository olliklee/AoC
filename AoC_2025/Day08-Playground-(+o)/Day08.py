# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from itertools import combinations
from math import dist, prod


year, day = "2025", "08"


def insert_connection(connection_map, spot1, spot2):
    matches = [c for c in connection_map if (spot1 in c or spot2 in c)]

    if not matches:
        connection_map.append({spot1, spot2})
        return

    # wenn es mindestens eine passende Verbindung gibt, vereinige alles in die erste
    base = matches[0]
    base.add(spot1)
    base.add(spot2)

    # falls es noch weitere matches gibt (verschiedene Sets, die zusammengehören),
    # dann merge sie in base und entferne die anderen aus connection_map
    for extra in matches[1:]:
        base.update(extra)
        connection_map.remove(extra)


def solve():
    test = False
    max_circuits = 10 if test else 1000
    part1 = part2 = 0
    puzzle = load_input(test=test, split_by_line=True)
    junctions = [tuple(map(int,line.split(','))) for line in puzzle]
    distances = {(p1, p2): dist(p1, p2) for p1, p2 in combinations(junctions,2)}
    sorted_distances = iter(dict(sorted(distances.items(), key=lambda item: item[1])).keys())

    connected_spots = set()
    connection_map = []
    i= 0

    while True:
        spot1, spot2 = next(sorted_distances)

        if i >= max_circuits:
            circuits = sorted([len(connection) for connection in connection_map], reverse=True)
            if i == max_circuits:
                part1 = prod(circuits[:3])

            if circuits[0] == 1000:
                print(i, spot1, spot2, circuits[0])
                part2 = spot1[0] * spot2[0]
                break

        insert_connection(connection_map, spot1, spot2)
        connected_spots.add(spot1)
        connected_spots.add(spot2)
        i += 1

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)


# 5309750420 too high

