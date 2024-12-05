from time import perf_counter
from typing import Callable, Tuple


def load_input(test=False, split_by_line=False, delimiter='') -> str:
    """ Read main input or test input from this folder.It returns the file as string """

    file_name = f"input_.txt" if test else f"input.txt"
    split_character = '\n' if split_by_line and not delimiter else delimiter
    try:
        with open(file_name, 'r') as fd:
            content = fd.read()
    except FileNotFoundError:
        print(f"File {file_name} not found.")

    return content.split(split_character) if split_character else content


def run_puzzles(d:str, y:str, result_a: Callable[[], int], result_b: Callable[[], int]):
    """ Call result formulas without () """

    start = perf_counter()
    part_a = result_a()
    lap = perf_counter()
    part_b = result_b()
    stop = perf_counter()

    print(f'''
      Results from AoC {y} - Day {d}
    {'-' * 34}
      Part 1: {part_a} ({(lap - start) * 100:.6f} ms)
      Part 2: {part_b} ({(stop - lap) * 100:.6f} ms)
    {'-' * 34}
      Time complete: {(stop - start) * 100:.6f} ms
    ''')


def run_puzzle(d:str, y:str, result: Callable[[], Tuple[int, int]]) -> None:
    """ call result formula without () """

    start = perf_counter()
    part_a, part_b = result()
    stop = perf_counter()

    print(f'''
      Results from AoC {y} - Day {d}
    {'-' * 34}
      Part 1: {part_a}
      Part 2: {part_b}
    {'-' * 34}
      Time: {(stop - start) * 100:.6f} ms
    ''')
