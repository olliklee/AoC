from time import perf_counter
from typing import Callable

def load_input(day: str, test=False) -> str:
    '''Read main input or test input from this folder.
    It returns the file as string'''
    file_name = f"Day{day}_input_.txt" if test else f"Day{day}_input.txt"

    with open(file_name) as fd:
        content = fd.read()
    return content

def run_puzzles(d:str, y:str, result_a: Callable[[], int], result_b: Callable[[], int]):
    ''' call result formulas without () '''
    print(f"\nResults from AoC {y} - Day {d}\n{'-' * 30}")

    start = perf_counter()
    print(f"Day {d} - Part 1: {result_a()}")

    lap = perf_counter()
    print(f"Day {d} - Part 2: {result_b()}")

    stop = perf_counter()

    print(f"\nPerformance\n{'-' * 30}")
    print(f"Part 1: {(lap - start) * 100:.6f} ms\nPart 2: {(stop - lap) * 100:.6f} ms")
    print(f"{'-' * 30}\nGesamt: {(stop - start) * 100:.6f} ms")

