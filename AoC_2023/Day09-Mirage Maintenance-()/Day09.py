# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

from re import findall

year, day = "2023", "09"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final


def prepare_input(file_name):
    with open(file_name) as f:
        content = [list(map(int, findall("\d+", row))) for row in f.read().split("\n")]

    return content


def analyze(sequence):
    sequences = [sequence]
    while not all( [element == 0 for element in sequences[-1]]):
        reduced_sequence = []
        act_sequence = sequences[-1]

        for i in range(len(act_sequence) - 1):
            reduced_sequence.append(act_sequence[i + 1] - act_sequence[i])
        sequences.append(reduced_sequence)

    for i in range(len(sequences) -1, 0, -1):
        act_sequence = sequences[i]
        sequences[i-1].append(act_sequence[-1] + sequences[i-1][-1])
        print(sequences[i-1])
    print(sequences[0][-1])
    return sequences[0][-1]

def solve_a():

    return sum([analyze(row) for row in puzzle])


def solve_b():
    return 0


#  ----------   Start   ----------   #

puzzle = prepare_input(filename)
run_puzzles(day, year, solve_a, solve_b)

'''2382245591 wrong
2382245549 too high'''