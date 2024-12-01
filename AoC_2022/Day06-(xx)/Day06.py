# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter

year, day = "2022", "06"


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
        return f.read()


def solve_a():
    signal = prepare_input(f"Day{day}_input.txt")
    pl = 4  # packet_length
    return [i + pl for i in range(len(signal)-pl) if len(set(signal[i:i + pl])) == pl][0]


def solve_b():
    signal = prepare_input(f"Day{day}_input.txt")
    pl = 14  # packet_length
    return [i + pl for i in range(len(signal)-pl) if len(set(signal[i:i + pl])) == pl][0]


run(day, year)
