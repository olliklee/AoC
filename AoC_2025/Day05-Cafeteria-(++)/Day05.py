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

    prev_start, prev_stop = intervals[0]
    for start, stop in intervals[1:]:
        if start <= prev_stop + 1:
            prev_stop = max(prev_stop, stop)  # bei Überschneidung
        else:
            part2 += prev_stop - prev_start + 1  # länge des intervalls zur gesamtzahl addieren
            prev_start, prev_stop = start, stop  # neues intervall starten

    part2 += prev_stop - prev_start + 1  # letztes intervall noch zur gesamtzahl addieren

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
