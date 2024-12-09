# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2024", "09"

def solve():
    part1 = part2 = 0

    puzzle = list(map(int, list(load_input(test=False))))

    storage = []
    file_id = 0
    for i in range(0, len(puzzle), 2):

        storage.extend(puzzle[i] * [str(file_id)])
        if i < len(puzzle) - 1: storage.extend(list(puzzle[i + 1] * '.'))
        file_id += 1

    free = storage.count('.')

    # move files into free spot
    for i in range(free):
        last = storage.pop()

        if last != '.':
            storage[storage.index('.')] = str(last)

    print("compressed")

    # calc checksum
    part1 = sum([i * int(id) for i, id in enumerate(storage)])

    return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)