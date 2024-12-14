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


def run_puzzle(d:str, y:str, result) -> None:
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


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def print_matrix(matrix):
    if type(matrix) is dict:
        max_x = max(key[0] for key in matrix.keys())
        max_y = max(key[1] for key in matrix.keys())

        # Drucke das Gitter basierend auf den Koordinaten
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                # Überprüfe, ob die Koordinate im Dictionary existiert
                if (x, y) in matrix:
                    print(matrix[(x, y)], end=" ")
                else:
                    print(".", end=" ")  # Leere Felder mit einem Punkt füllen
            print()  # Neue Zeile für das nächste x
        print()
    elif type(matrix) is list:
        for row in matrix:
            print(" ".join(val for val in row))  # :2 für einheitliche Spaltenbreite
        print()