#  Solutions of Advent of Code
#  Oliver Kleemann

from time import perf_counter

year, day = "2022", "04"

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
    with open(file_name) as f:
        sections = []
        for pair in f:
            elf1, elf2 = pair.strip().split(",")
            elf1, elf2 = elf1.split("-"), elf2.split("-")
            elf1 = set(range(int(elf1[0]), int(elf1[1]) + 1))
            elf2 = set(range(int(elf2[0]), int(elf2[1]) + 1))
            sections.append([elf1, elf2])
    return sections


def solve_a():
    sections = prepare_input(f"Day{day}_input.txt")
    counter = 0
    for section in sections:
        elf1, elf2 = section
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            counter += 1
    return counter


def solve_b():
    sections = prepare_input(f"Day{day}_input.txt")
    counter = 0
    for section in sections:
        elf1, elf2 = section
        if len(elf1.intersection(elf2)) > 0:
            counter += 1
    return counter


run(day, year)
