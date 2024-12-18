# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

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

## solution from Gravitar (https://github.com/Gravitar64/Advent-of-Code-2024/blob/master/day09.py)
def compress2(puzzle):
        files, spaces = dict(), []
        pos = 0
        for i, n in enumerate(puzzle):
            if i % 2:
                spaces.append((pos, n))
            else:
                files[i // 2] = (pos, n)
            pos += n
        
        for f_id, (file_pos, file_size) in reversed(files.items()):
            for i, (space_pos, space_size) in enumerate(spaces):
                if space_pos >= file_pos: break
                if file_size > space_size: continue
                
                files[f_id] = (space_pos, file_size)
                new_space_size = space_size - file_size
                
                if new_space_size == 0:
                    spaces.pop(i)
                else:
                    spaces[i] = (space_pos + file_size, new_space_size)
                break
        return sum(sum(f_id * n for n in range(p, p + l)) for f_id, (p, l) in files.items())


def solve():
    puzzle = list(map(int, list(load_input(test=False))))

    storage = defaultdict(tuple)
    file_id = 0
    for i in range(0, len(puzzle) - 1, 2):
        storage[file_id] = (puzzle[i], puzzle[i + 1])
        file_id += 1
    storage[file_id] = (puzzle[-1], 0)
    
    part1 = sum([i * int(file_id) for i, file_id in enumerate(compress1(storage))])
    
    part2 = compress2(puzzle)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
