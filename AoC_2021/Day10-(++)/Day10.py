# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = '2021', '10'


def remove_chunks(data):
    startcount = 1
    endcount = 0
    while startcount != endcount:
        startcount = len(data)
        data = data.replace("()", "").replace("[]", "").replace("{}", "").replace("<>", "")
        endcount = len(data)

    return data


def is_incompete(data):
    for sign in data:
        if sign in ")]}>":
            return False
    return True


def part1():
    riddle = load_input(split_by_line=True)
    closeings = ")]}>"
    score_table = {')':3, ']':57, '}':1197, '>':25137}
    score = 0
    for data in riddle:
        # Remove all "()", "[]", ...
        data = remove_chunks(data)

        # Find first corruption and add its value to the total score
        for sign in data:
            if sign in closeings:
                score += score_table.get(sign, 0)
                break  # only first corruption counts

    return score

def part2():
    riddle = load_input(split_by_line=True)
    according_bracket = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_table = {')': 1, ']': 2, '}': 3, '>': 4}

    total_score = []

    for data in riddle:
        # Remove all "()", "[]", ...
        data = remove_chunks(data)

        # if not corrupted, just incomplete: fill missing closing characters
        completion = []
        if is_incompete(data):
            for i in range(len(data)):
                completion.insert(0, according_bracket[data[i]])

            # scoring
            score = 0
            for sign in completion:
                score *= 5
                score += score_table.get(sign, 0)

            total_score.append(score)

    middle_score = sorted(total_score)[len(total_score) // 2]
    return middle_score

run_puzzles(day, year, part1, part2)
