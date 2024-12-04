# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
year, day = "2021", "01"

def solve():
    zahlen = list(map(int, load_input().split('\n')))

    result_a = result_b = 0
    index = 0
    while index < len(zahlen) - 1:
        if zahlen[index + 1] > zahlen[index]:
            result_a += 1
        index += 1

    sum1 = 0
    index = 0
    while index < len(zahlen) - 3:
        sum2 = sum(zahlen[index:index+2])

        if sum2 > sum1:
            result_b += 1
        sum1 = sum2
        index += 1

    return result_a, result_b


### ----------- Start ------------- ###

run_puzzle(year, day, solve)