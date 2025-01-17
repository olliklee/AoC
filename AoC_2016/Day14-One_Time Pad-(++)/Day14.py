# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from hashlib import md5
import re

year, day = "2016", "14"


def has_triples(word):
    match = re.search(r'(.)\1\1', word)
    return match.group(1) if match else None


def has_fivefolds(word):
    match = re.search(r'(.)\1\1\1\1', word)
    return match.group(1) if match else None


def md5_stretching(input_string, times=2016):
    result = md5(input_string.encode()).hexdigest()
    for _ in range(times):
        result = md5(result.encode()).hexdigest()
    return result


def create_keys(puzzle, keys, potential_keys, fivefold_cache, stretching=False):
    i = 0
    while len(keys) < 64:
        # Normales oder gestretchtes Hashing
        hash_function = md5_stretching if stretching else lambda x: md5(x.encode()).hexdigest()
        word = hash_function(f'{puzzle}{i}')

        if t := has_triples(word):
            potential_keys[i] = t

        if f := has_fivefolds(word):
            fivefold_cache[i] = f

        for kt, vt in list(potential_keys.items()):  # Gehe durch die gespeicherten Triples
            for kf, vf in fivefold_cache.items():  # Gehe durch die gespeicherten Fivefolds
                if vt == vf and 0 < kf - kt <= 1000:
                    keys.append(kt)  # Füge den Index als gültigen Schlüssel hinzu
                    del potential_keys[kt]  # Entferne das bestätigte Triple
                    break

        i += 1  # Nächster Index

    return keys[63]


def solve():
    test = False
    puzzle = 'abc' if test else 'zpqevtbw'

    keys = []  # Liste für die validen Schlüssel
    potential_keys = {}  # Indizes mit Triple-Zeichen
    fivefold_cache = {}  # Indizes mit Fivefold-Zeichen
    part1 = create_keys(puzzle, keys, potential_keys, fivefold_cache)

    keys.clear() # Liste für die validen Schlüssel
    potential_keys.clear()
    fivefold_cache.clear()
    part2 = create_keys(puzzle, keys, potential_keys, fivefold_cache, stretching=True)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
