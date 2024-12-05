# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

from math import pow
from collections import defaultdict

year, day = "2023", "04"



def calculate_win(win_dict, puzzle, card_id):
    win_nums, my_nums = puzzle[card_id]
    matches = -1
    crd_val = 0
    for win_num in win_nums:
        if win_num in my_nums:
            matches += 1

    if matches != -1:
        crd_val = int(pow(2, matches))

    win_dict[card_id] = matches + 1  # count of matching numbers for part 2

    return crd_val


def solve():
    win_dict = {}
    copy_dict = defaultdict(lambda: 1)

    puzzle = {int(card.split(':')[0].split()[1]): \
                  (card.split(':')[1].split('|')[0].strip().split(),
                   card.split('|')[1].strip().split()) for card in load_input(split_by_line=True)}

    part1 = sum(calculate_win(win_dict, puzzle, card_id) for card_id in puzzle.keys())

    part2 = sum(copy_dict[card_id] + \
                sum(copy_dict[i] for i in range(card_id + 1, card_id + win_dict[card_id] + 1)) \
                for card_id in win_dict.keys())

    return part1, part2


### ----------- Main ------------- ###


run_puzzle(day, year, solve)
