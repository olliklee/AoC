from time import perf_counter


def run(d, y, result_a, result_b):
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
