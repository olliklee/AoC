# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

from math import pow
from collections import defaultdict

year, day = "2023", "04"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final

win_dict = {}
copy_dict = defaultdict(lambda: 1)


def prepare_input(file_name):
    with open(file_name) as f:
        content = f.read().split("\n")

    # card dictionary { id: ([win_nums, my_nums]) }
    return {int(card.split(':')[0].split()[1]): \
                (card.split(':')[1].split('|')[0].strip().split(),
                 card.split('|')[1].strip().split())
            for card in content}


def calculate_win(card_id):
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


def solve_a():
    result = 0
    for card_id in puzzle.keys():
        crd_val = calculate_win(card_id)
        result += crd_val
    return result


def solve_b():
    result = 0
    for card_id in win_dict.keys():
        for i in range(card_id + 1, card_id + win_dict[card_id] + 1):
            copy_dict[i] += copy_dict[card_id]
        result += copy_dict[card_id]
    return result


### ----------- Main ------------- ###

puzzle = prepare_input(filename)
run_puzzles(day, year, solve_a, solve_b)