# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter
from collections import deque

year, day = "2022", "20"
final = f"input/Day{day}_input.txt"
test = f"input/Day{day}_input_.txt"
filename = test


def run(d, y):
    print(f"\nResults from AoC {y} - Day {d}\n{'-' * 30}")

    start = perf_counter()
#    print(f"Day {d} - Part 1: {solve_a()}")

    lap = perf_counter()
    print(f"Day {d} - Part 2: {solve_b()}")

    stop = perf_counter()

    print(f"\nPerformance\n{'-' * 30}")
    print(f"Part 1: {(lap - start) * 100:.6f} ms\nPart 2: {(stop - lap) * 100:.6f} ms")
    print(f"{'-' * 30}\nGesamt: {(stop - start) * 100:.6f} ms")


def prepare_input(file_name):
    with open(file_name) as f:
        return enumerate(list(map(int, f.read().split("\n"))))


init_data = deque(prepare_input(filename))
length = len(init_data)

def solve_a():
    mix_data = init_data.copy()
    i_for_0 = 0
    for i, val in init_data:
        if val == 0:
            i_for_0 = i
        pos = mix_data.index((i, val))
        mix_data.rotate(-pos)
        mix_data.popleft()
        mix_data.rotate(-val)
        mix_data.appendleft((i,val))

    zero_index = mix_data.index((i_for_0,0))
    solution = sum((mix_data[(zero_index + 1000) % length][1],
               mix_data[(zero_index + 2000) % length][1],
               mix_data[(zero_index + 3000) % length][1]))

    return solution


def solve_b():
    mix_data: deque[(int,int)]
    for i, val in init_data:
        mix_data[i] = (int, val * 811589153)

    print(mix_data)


    return None


run(day, year)

