# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2022", "13"


def correct(left, right):
    if type(left) is list or type(right) is list:
        if type(left) is not list: left = [left]
        if type(right) is not list: right = [right]
        for l, r in zip(left, right):
            c = correct(l, r)
            if c != 0: return c
        return len(left) - len(right)
    else:
        return left - right


def solve():
    inp = [eval(line.strip())
           for line in load_input(split_by_line=True)
           if line > ' ']
    
    # part1
    part1 = 0
    for i, (left, right) in enumerate(zip(inp[::2], inp[1::2]), 1):
        if correct(left, right) >= 0: continue
        part1 += i
    
    # part2
    inp.append([[6]])
    inp.append([[2]])
    
    sorted_list = inp.copy()
    #   Bubble sort, if I remember right
    counter = 1
    while True:
        all_packets_sorted = True
        
        for i in range(len(sorted_list) - counter):
            compared = correct(sorted_list[i], sorted_list[i + 1])
            if compared == 0:
                continue
            elif compared > 0:
                sorted_list.insert(i, sorted_list.pop(i + 1))  # switch order
                all_packets_sorted = False
        counter += 1
        if all_packets_sorted:
            break
    
    part2 = (sorted_list.index([[2]]) + 1) * (sorted_list.index([[6]]) + 1)
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
