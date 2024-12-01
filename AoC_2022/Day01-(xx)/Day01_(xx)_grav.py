#  Solutions of Advent of Code
#  Oliver Kleemann

from time import perf_counter

year, day = "2022", "01"


def run(d, y):
    print(f"\nResults from AoC {y} - Day {d}\n{'-' * 30}")

    start = perf_counter()
    print(f"Day {d} - Part 1: {solve()[0]}")

    lap = perf_counter()
    print(f"Day {d} - Part 2: {solve()[1]}")

    stop = perf_counter()

    print(f"\nPerformance\n{'-' * 30}")
    print(f"Part 1: {(lap - start) * 100:.6f} ms\nPart 2: {(stop - lap)*100:.6f} ms")
    print(f"{'-' * 30}\nGesamt: {(stop - start)*100:.6f} ms")


def prepare_input(file_name):
    with open(file_name) as f:
        return sorted([sum(int(calories) for calories in elve.split("\n")) for elve in f.read().split("\n\n")], reverse=True)


def solve():
    elves_inventory = prepare_input("../AoC 2022/input/Day01_input.txt")
    return elves_inventory[0], sum(elves_inventory[:3])



run(day, year)
