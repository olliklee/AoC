# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from random import sample

year, day = "2021", "08"


def read_input_from_file_b(file_name):
    data = []
    with open(file_name) as f:
        for line in f:
            line = line.strip().split("|")
            data.append(line[0].split())
            data.append(line[1].split())

    return data


def is_valid_element(digit):
    valid_values = [['a', 'b'], ['a', 'c', 'd', 'f', 'g'],
                    ['a', 'b', 'c', 'f', 'g'], ['a', 'b', 'e', 'g'],
                    ['b', 'c', 'e', 'f', 'g'], ['b', 'c', 'd', 'e', 'f', 'g'],
                    ['a', 'b', 'f'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                    ['a', 'b', 'c', 'e', 'f', 'g'], ['a', 'b', 'c', 'd', 'e', 'f']]
    return digit in valid_values


def get_shuffle_dictionary():
    dictionary = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g'}

    shuffled_values = sample(list(dictionary.values()), len(dictionary))
    shuffled_dictionary = dict(zip(dictionary.keys(), shuffled_values))
    return shuffled_dictionary


def translate_digit(code, dictionary):
    return [dictionary[letter] for letter in code]


def get_decimal(code):
    translator = {'ab': 1, 'acdfg': 2, 'abcfg': 3, 'abeg': 4, 'bcefg': 5,
                  'bcdefg': 6, 'abf': 7, 'abcdefg': 8, 'abcefg': 9, 'abcdef': 0}
    return translator[code]


def solve():
    puzzle1 = [word for line in load_input(split_by_line=True) for word in line.strip().split("|")[1].split()]
    possible_lengths = [2, 3, 4, 7]
    part1 = sum([True for code in puzzle1 if len(code) in possible_lengths])

    # Part 2
    puzzle2 = [part.split() for line in load_input(split_by_line=True) for part in line.strip().split("|")]
    part2 = 0  # Endergebnis
    for index in range(0, len(puzzle2), 2):
        frontpart = puzzle2[index]
        backpart = puzzle2[index + 1]

        # Erstellt Codeentschlüsselung in dem eine zufällige Key-Matrix
        # auf richtige Ergebnisse getestet wird. Random Brute Force Verfahren.
        while True:
            dictionary = get_shuffle_dictionary()
            solved_counter = 0

            for code in frontpart:
                new_code = sorted(translate_digit(code, dictionary))
                if is_valid_element(new_code):
                    solved_counter += 1

            if solved_counter >= len(frontpart):
                print(".", end='')
                break

        code_key = dictionary  # passender Code gefunden

        # Übersetze falsche Signale
        lst = [get_decimal(''.join(sorted(translate_digit(code, code_key)))) for code in backpart]

        # Addiere die letzten 4-stelligen Zahlen
        solution_of_row = int(''.join([str(item) for item in lst]))
        part2 += solution_of_row

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
