# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import Counter

import re

year, day = "2016", "04"


def is_valid(text, checksum):
    counter = Counter(text.replace('-', ''))
    commons = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:5]
    word = ''.join([item[0] for item in commons])
    return word == checksum


def solve():
    puzzle = load_input(test=False)
    pattern = r'^([a-z-]+)-(\d+)\[([a-z]+)\]$'
    matches = re.findall(pattern, puzzle, re.MULTILINE)

    # remove decoys
    real_rooms = [line for line in matches if is_valid(line[0], line[2])]
    storage_room_id = 0

    for room in real_rooms:
        shift = int(room[1]) % 26
        decrypted = ''
        for letter in room[0]:
            if letter == "-":
                decrypted += ' '
            else:
                decrypted += chr(((ord(letter) - 97) + shift) % 26 + 97)

        if decrypted == 'northpole object storage':
            storage_room_id = room[1]
            break

    part1 = sum([int(room[1]) for room in real_rooms])
    part2 = storage_room_id

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
