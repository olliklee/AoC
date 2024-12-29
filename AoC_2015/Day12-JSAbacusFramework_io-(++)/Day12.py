# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

import json

from aoc_helper import *

year, day = "2015", "12"

result = 0


def analyze_json_a(json_obj, parent_key=""):
    global result

    if type(json_obj) is dict:
        for key, value in json_obj.items():
            new_key = f"{parent_key}['{key}']" if parent_key else key
            analyze_json_a(value, new_key)
    elif type(json_obj) is list:
        for index, value in enumerate(json_obj):
            new_key = f"{parent_key}[{index}]"
            analyze_json_a(value, new_key)
    else:
        try:
            result += int(json_obj)
        except ValueError:
            pass


def analyze_json_b(json_obj, parent_key=""):
    global result
    if type(json_obj) is dict:
        if 'red' not in json_obj.values():
            for key, value in json_obj.items():
                new_key = f"{parent_key}['{key}']" if parent_key else key
                analyze_json_b(value, new_key)
    elif type(json_obj) is list:
        for index, value in enumerate(json_obj):
            new_key = f"{parent_key}[{index}]"
            analyze_json_b(value, new_key)
    else:
        try:
            result += int(json_obj)
        except ValueError:
            pass


def solve():
    puzzle = load_input()

    decoder = json.JSONDecoder()
    my_json = decoder.decode(puzzle)
    global result

    result = 0
    analyze_json_a(my_json)
    part1 = result

    result = 0
    analyze_json_b(my_json)
    part2 = result

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
