from time import perf_counter

def run_puzzles(d: str, y: str, func_a, func_b):
    """ This function is specially for the adventofcode project.
    The parameters are:
    Day and year as String,
    Two functions for part1 and part2.
    It prints out the results of the two functions and the time it took to solve it."""

    edge = '-' * 26
    dotted = "|" + '-' * 24 + '|'

    print(f"{edge}\n"
          f"|   AoC {y} - Day {d}    |\n"
          f"{dotted}")

    start = perf_counter()
    print(f"|  Part 1: {func_a():<14.0f}|")
    lap = perf_counter()
    print(f"|  Part 2: {func_b():<14.0f}|")
    stop = perf_counter()

    print(f"{edge}\n"
          f"|      Performance       |\n"
          f"{dotted}\n"
          f"|  Part 1: {(lap - start) * 100:>7.4f} ms    |\n"
          f"|  Part 2: {(stop - lap) * 100:>7.4f} ms    |\n"
          f"{dotted}\n"
          f"|   Total: {(stop - start) * 100:>7.4f} ms    |\n"
          f"{edge}")
