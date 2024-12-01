#  Solutions of Advent of Code
#  Oliver Kleemann

from AoC_2022.aoc_helper import run

year, day = "2022", "01"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final

def prepare_input(file_name):
    with open(file_name) as f:
        calories = []
        for line in f:
            line = line.strip()
            calories.append(line)
    # sum up calories for each elv
    sumup = 0
    elves = []
    for num in calories:
        if num != "":
            sumup += int(num)
        else:
            elves.append(sumup)
            sumup = 0

    elves.sort(reverse=True)
    return elves


def solve_a():
    # winner is:
    return elves[0]


def solve_b():
    # top 3 are:
    return sum(elves[:3])

elves = prepare_input(filename)

run(day, year, solve_a, solve_b)
