# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter
import json

year, day = "2022", "13"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final


def run(d, y):
    print(f"\nResults from AoC {y} - Day {d}\n{'-' * 30}")

    start = perf_counter()
    print(f"Day {d} - Part 1: {solve_a()}")

    lap = perf_counter()
    print(f"Day {d} - Part 2: {solve_b()}")

    stop = perf_counter()

    print(f"\nPerformance\n{'-' * 30}")
    print(f"Part 1: {(lap - start) * 100:.6f} ms\nPart 2: {(stop - lap) * 100:.6f} ms")
    print(f"{'-' * 30}\nGesamt: {(stop - start) * 100:.6f} ms")


def prepare_input(file_name):
    output = []
    with open(file_name) as f:
        return [eval(line.strip()) for line in f.readlines() if line > ' ']


def correct(left, right):
    if type(left) is list or type(right) is list:
        if type(left) is not list: left = [left]
        if type(right) is not list: right = [right]
        for l,r in zip(left,right):
            c = correct(l,r)
            if c != 0: return c
        return len(left) - len(right)
    else:
        return left - right


def solve_a():
    inp = prepare_input(filename)
    solution = 0
    for i, (left, right) in enumerate(zip(inp[::2], inp[1::2]), 1):
        if correct(left, right) >= 0: continue
        solution += i
    return solution

def solve_b():
    inp = prepare_input(filename)
    inp.append([[6]])
    inp.append([[2]])

    sorted_list = inp.copy()
    #   Bubble sort, if i remember right
    counter = 1
    while True:
        all_packets_sorted = True

        for i in range(len(sorted_list) - counter):
            compared = correct(sorted_list[i],sorted_list[i+1])
            if compared == 0:
                continue
            elif compared > 0:
                sorted_list.insert(i,sorted_list.pop(i+1))  # switch order
                all_packets_sorted = False
        counter += 1
        if all_packets_sorted:
            break

    return (sorted_list.index([[2]])+1) * (sorted_list.index([[6]])+1)


run(day, year)
