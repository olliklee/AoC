from time import perf_counter


def load_input(day, test=False):
    final_name = f"Day{day}_input.txt"
    test_name = f"Day{day}_input_.txt"
    filename = test_name if test else final_name
    with open(filename) as fd:
        content = fd.read()
    return content


def run_puzzles(d, y, result_a, result_b):
    print(f"\nResults from AoC {y} - Day {d}\n{'-' * 30}")

    start = perf_counter()
    print(f"Day {d} - Part 1: {result_a()}")

    lap = perf_counter()
    print(f"Day {d} - Part 2: {result_b()}")

    stop = perf_counter()

    print(f"\nPerformance\n{'-' * 30}")
    print(f"Part 1: {(lap - start) * 100:.6f} ms\nPart 2: {(stop - lap) * 100:.6f} ms")
    print(f"{'-' * 30}\nGesamt: {(stop - start) * 100:.6f} ms")


def print_matrix(matrix):
    for y in range(-12, 30):
        display = f"{y:3} "
        for x in range(-12, 30):
            if (x, y) in matrix:
                display += "#"
            else:
                display += "."
        print(display)
