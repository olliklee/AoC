#  Solutions of Advent of Code
#  Oliver Kleemann

from time import perf_counter

year, day = "2022", "03"

test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def prepare_input(file_name):
    with open(file_name) as f:
        rucksack = []
        for line in f:
            line = line.strip()
            rucksack.append(line)
    return rucksack


def solve_a():
    rucksacks = prepare_input(f"Day{day}_input.txt")
    score = 0
    # split bags in 2 compartments and find the common item
    for bag in rucksacks:
        compartment1 = bag[:len(bag) // 2]
        compartment2 = bag[len(bag) // 2:]
        in_both = list(set(compartment1).intersection(set(compartment2)))[0]
        score += (ord(in_both) - 96) + (58 if in_both.isupper() else 0) # calculation with ascii

    return score


def solve_b():
    rucksacks = prepare_input(f"Day{day}_input.txt")
    score = 0

    # split into teams of 3
    teams = []
    for i in range(0, len(rucksacks), 3):
        teams += ((rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]),)

    # find the badge of each team
    for team in teams:
        badge = list(set(team[0]).intersection(set(team[1]).intersection((set(team[2])))))[0]
        score += (ord(badge) - 96) + (58 if badge.isupper() else 0) # calculation with ascii

    return score


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


run(day, year)
