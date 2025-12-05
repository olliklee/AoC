# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2025", "05"


def is_fresh(ranges, ingredient):
    for minimum, maximum in ranges:
        if minimum <= ingredient <= maximum:
            return True
    return False
    # 30% langsamer:
    # return any(minimum <= ingredient <= maximum for minimum, maximum in ranges)


def solve():
    ids, ingredients = (line.split('\n') for line in load_input(test=False, split_by_line=True, delimiter='\n\n'))

    intervals = [tuple(map(int, ii.split('-'))) for ii in ids]
    ingredients = list(map(int, ingredients))

    part1 = len([ingredient for ingredient in ingredients if is_fresh(intervals, ingredient)])

    part2 = 0
    intervals.sort()  # sortiert nach start wert des tuples

    # noinspection PyTypeChecker
    act_start, act_stop = intervals[0]
    for start, stop in intervals[1:]:
        if start <= act_stop + 1:
            act_stop = max(act_stop, stop)  # bei Überschneidung
        else:
            part2 += act_stop - act_start + 1  # länge des intervalls zur gesamtzahl addieren
            act_start, act_stop = start, stop  # neues intervall starten

    part2 += act_stop - act_start + 1  # letztes intervall zur gesamtzahl addieren

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
