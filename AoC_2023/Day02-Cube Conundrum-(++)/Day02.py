# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2023", "02"


def solve_a():
    id_sum = 0
    max_possible = {'red': 12, 'green': 13, 'blue': 14}

    for game in puzzle:
        game_id = int(game.split(':')[0].replace('Game ', ''))
        game_results = game.split(':')[1].strip().split(';')

        valid = True
        for turn in game_results:
            color_dict = {c.split()[1]: int(c.split()[0]) for c in turn.split(', ')}

            for key, value in color_dict.items():
                if value > max_possible[key]:
                    valid = False
                    break

        if valid:
            id_sum += game_id

    return id_sum


def solve_b():
    id_sum = 0

    for game in puzzle:
        game_results = game.split(':')[1].strip().split(';')

        maxred, maxgreen, maxblue = 0, 0, 0
        for turn in game_results:
            color_dict = {c.split()[1]: int(c.split()[0]) for c in turn.split(', ')}

            maxred = max(maxred, color_dict.get("red", 0))
            maxgreen = max(maxgreen, color_dict.get("green", 0))
            maxblue = max(maxblue, color_dict.get("blue", 0))

        id_sum += maxred * maxblue * maxgreen

    return id_sum


puzzle = load_input().split('\n')
run_puzzles(day, year, solve_a, solve_b)
