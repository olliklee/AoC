# # #  Solutions of Advent of Code
# # #  Oliver Kleemann
from calendar import firstweekday

from aoc_helper import *
from collections import defaultdict

year, day = "2024", "09"


def compress1(storage):
    new_storage = []
    max_id = len(storage) - 1
    f_pointer, b_pointer = -1, max_id
    to_fill, fillers = 0, storage[max_id][0]

    while True:
        if to_fill == 0:
            f_pointer += 1
            if f_pointer == b_pointer:
                new_storage.extend([f_pointer] * fillers)
                break
            new_storage.extend([f_pointer] * storage[f_pointer][0])
            to_fill = storage[f_pointer][1]

        while to_fill > 0:
            if fillers == 0:
                b_pointer -= 1
                fillers = storage[b_pointer][0]
                break

            new_storage.extend([b_pointer])
            to_fill -= 1
            fillers -= 1
    return new_storage

def compress2(storage):
    new_storage = []
    moved = []
    free = {key: int(file[1])  for key, file in storage.items()}# when a block is moved to begin, the id is copied here

    max_id = len(storage) - 1
    f_pointer, b_pointer = 0, max_id

    new_storage.extend([f_pointer] * storage[0][0])
    while free:
        print(new_storage)
        gap = free[f_pointer]
        if b_pointer in moved:
            b_pointer -= 1
            continue
        while True:
            size = storage[b_pointer][0]
            if size < gap:
                new_storage.extend(size * [b_pointer])
                free[f_pointer] -= size
                moved.append(b_pointer)
                break
            elif size == gap:
                new_storage.extend(size * [b_pointer])
                moved.append(b_pointer)
                del free[f_pointer]
                f_pointer += 1
                b_pointer = max_id

                break
            else:
                b_pointer -= 1
                if b_pointer <= f_pointer:
                    new_storage.extend(size * '.')
                    f_pointer += 1
                    b_pointer = max_id
                    break

def compress3(storage):
    liste = []
    new_storage = [item for k, v in storage.items() for item in ([k] * v[0] + v[1] * ["."])]
    last = new_storage[-1]
    while True:
        for i in range(1, len(new_storage)):
        last = new_storage[-1]
        if last


    return new_storage

def solve():
    puzzle = list(map(int, list(load_input(test=True))))

    storage = defaultdict(tuple)
    file_id = 0
    for i in range(0, len(puzzle) - 1, 2):
        storage[file_id] = (puzzle[i], puzzle[i + 1])
        file_id += 1
    storage[file_id] = (puzzle[-1], 0)




    # part1 = sum([i * int(file_id) for i, file_id in enumerate(compress1(storage))])
    # part2 = sum([i * int(file_id) for i, file_id in enumerate(compress2(storage)) if file_id != '.'])
    print(compress3(storage))
    return 0,0


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
