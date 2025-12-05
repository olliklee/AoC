# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re
from collections import defaultdict
import random
from itertools import product

year, day = "2015", "15"

ing_dict = defaultdict(list)


def init_ingredients():
    puzzle = load_input(test=False).split('\n')
    for line in puzzle:
        ing, vals = line.split(':')
        cap, dur, fla, tex, cal = map(int, re.findall(r'(-?\d+)', vals))
        ing_dict[ing] = [cap, dur, fla, tex, cal]
    print(ing_dict)


def get_variants(amount):
    yield (for combination in product(range(100 + 1), repeat=amount) if sum(combination) == 100)
    

def neighbor(amounts):
    new_amounts = amounts[:]
    idx1, idx2 = random.sample(range(len(new_amounts)), 2)  # Zwei zufällige Indizes
    change = random.randint(1, 5)  # Kleiner Schritt für feinere Suche

    # Zutat `idx1` verringern und `idx2` erhöhen, solange die Gesamtverteilung gültig bleibt
    if new_amounts[idx1] >= change:
        new_amounts[idx1] -= change
        new_amounts[idx2] += change

    return new_amounts


def calc_score(amounts):
    if sum(amounts) != 100:
        print("Not 100 spoons!")
        return 0, 0

    total_props = [0] * 5
    for amount, props in zip(amounts, ing_dict.values()):
        for i, prop in enumerate(props):
            total_props[i] += amount * prop

    if any(p < 0 for p in total_props[:-1]):
        return 0, total_props[4]

    score = total_props[0] * total_props[1] * total_props[2] * total_props[3]
    return score, total_props[4]


def solve():
    init_ingredients()
    count = len(ing_dict)
    amounts = [100// count] * count
    highest_score, _ = calc_score(amounts)

    # Teil 1: Höchster Score
    for _ in range(10000):  # Erhöhe Iterationen für bessere Ergebnisse
        neighbor_amounts = neighbor(amounts)
        score, _ = calc_score(neighbor_amounts)
        if score > highest_score:
            amounts = neighbor_amounts
            highest_score = score

    part1 = highest_score

    # Teil 2: Höchster Score mit 500 Kalorien
    amounts = [100 // count] * count
    highest_score = 0
    for _ in range(10000):  # Weitere Iterationen für Teil 2
        neighbor_amounts = neighbor(amounts)
        score, cals = calc_score(neighbor_amounts)
        if cals == 500 and score > highest_score:
            amounts = neighbor_amounts
            highest_score = score

    part2 = highest_score

    return part1, part2

#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
