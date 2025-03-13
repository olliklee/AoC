# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2023", "01"

int_dict = {"one": 1, "two": 2, "three": 3,
            "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9,
            "zero": 0}


def translate(text: str):
    new_text = ''
    for index, letter in enumerate(text):
        if letter.isdigit():
            new_text += letter
            continue
        
        for key in int_dict.keys():
            # Is the given index of the find method == the index from the enumeration?
            # if not just check the next int_dict entry
            if text.find(key, index) == index:
                # put the int from the dictionary into the translation string
                # and leave the dict iteration to get the next letter in the text string
                new_text += str(int_dict[key])
                break
    
    return new_text


def solve():
    puzzle = load_input(test=False, split_by_line=True)
    
    digits = [re.findall(r"(\d)", line) for line in puzzle]
    part1 = sum([int(d[0] + d[-1]) for d in digits])
    
    sum_up = 0
    for line in puzzle:
        new_line = translate(line)
        sum_up += int(new_line[0] + new_line[-1])
    
    part2 = sum_up
    
    return part1, part2


run_puzzle(day, year, solve)
