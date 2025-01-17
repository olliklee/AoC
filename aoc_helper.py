from time import perf_counter
from typing import Callable, TypeVar
import heapq

T = TypeVar("T", int, float, str)

DIVIDER = '-' * 41
DAY = lambda d: d[1:] if d[0] == '0' else d
HEADER = lambda y,d: f'Results from AoC {y} - Day {d}\n      https://adventofcode.com/{y}/day/{DAY(d)}\n'



def load_input(test=False, split_by_line=False, delimiter='') -> str:
    """ Read main input or test input from this folder.It returns the file as string """

    file_name = f"input_.txt" if test else f"input.txt"
    split_character = '\n' if split_by_line and not delimiter else delimiter
    try:
        with open(file_name, 'r') as fd:
            content = fd.read()
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    if not content:
        raise Exception('Empty input file.')

    return content.split(split_character) if split_character else content


def run_puzzles(d: str, y: str, result_a: Callable[[], int], result_b: Callable[[], int]):
    """ Call result formulas without () """

    start = perf_counter()
    part_a = result_a()
    lap = perf_counter()
    part_b = result_b()
    stop = perf_counter()

    print(f'''
    {DIVIDER}
      {HEADER(y, d)}
    {DIVIDER}
      Part 1: {part_a} ({(lap - start) * 100:.6f} ms)
      Part 2: {part_b} ({(stop - lap) * 100:.6f} ms)
    {DIVIDER}
      Time complete: {(stop - start) * 100:.6f} ms
      ->  https://adventofcode.com/{y}/day/{d}
    ''')


def run_puzzle(d: str, y: str, result) -> None:
    """ call result formula without () """

    start = perf_counter()
    part_a, part_b = result()
    stop = perf_counter()

    print(f'''
    {DIVIDER}
      {HEADER(y, d)}
    {DIVIDER}
      Part 1: {part_a}
      Part 2: {part_b}
    {DIVIDER}
      Time: {(stop - start) * 100:.6f} ms
    ''')


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def clamp(value: T, min_value: T, max_value: T) -> T:
    if min_value > max_value:
        raise ValueError("min_value must not be greater than max_value")
    return max(min(value, max_value), min_value)


def rotate_matrix(matrix, angle):
    if angle == 90:
        return [list(row) for row in zip(*matrix[::-1])]
    elif angle == 180:
        return [row[::-1] for row in matrix[::-1]]
    elif angle == 270:
        return [list(row) for row in zip(*matrix)][::-1]
    elif angle == 0:
        return matrix
    else:
        raise ValueError("Angle must be 0, 90, 180, or 270 degrees")


def print_matrix(matrix):
    """ print the map from a dictionary or a list"""
    if type(matrix) is dict:
        max_x = max(key[0] for key in matrix.keys())
        max_y = max(key[1] for key in matrix.keys())

        # Drucke das Gitter basierend auf den Koordinaten
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                # Überprüfe, ob die Koordinate im Dictionary existiert
                if (x, y) in matrix:
                    print(matrix[(x, y)], end=" ")
                else:
                    print(".", end=" ")  # Leere Felder mit einem Punkt füllen
            print()  # Neue Zeile für das nächste x
        print()
    elif type(matrix) is list:
        for row in matrix:
            print(" ".join(f"{val: 2}" for val in row))  # :2 für einheitliche Spaltenbreite
        print()


def convert_to_dict_map(map_as_string: str) -> dict:
    """
      Converts a multi-line ASCII map (given as a string) into a dictionary representation.

      Each character in the ASCII map is mapped to a coordinate (x, y), where:
        - `x` represents the horizontal position (column, starting at 0),
        - `y` represents the vertical position (row, starting at 0).

      The resulting dictionary uses:
        - Keys: Tuples `(x, y)` indicating the position in the grid.
        - Values: Characters from the ASCII map at the corresponding positions.
      """

    new_map = map_as_string.split("\n")
    return {(x, y): new_map[y][x] for y in range(len(new_map)) for x in range(len(new_map[y]))}


def dijkstra_map(map_data, start, goal):
    """
    Findet den kürzesten Pfad auf einer Karte von einem Start- zu einem Zielpunkt.

    Parameters:
        map_data (dict): Ein Dictionary mit Positionen (x, y) als Schlüssel und '.' oder '#' als Wert.
        start (tuple): Startposition als (x, y).
        goal (tuple): Zielposition als (x, y).

    Returns:
        list: Der kürzeste Pfad als Liste von (x, y)-Positionen, oder [] wenn kein Pfad gefunden wird.
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Nachbarpositionen (rechts, unten, links, oben)

    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    distances = {pos: float('inf') for pos in map_data}
    distances[start] = 0
    visited = set()  # Besuchte Felder
    while priority_queue:
        current_distance, current_pos, path = heapq.heappop(priority_queue)
        if current_pos in visited:
            continue
        visited.add(current_pos)

        # Ziel erreicht
        if current_pos == goal:
            return path

        # Nachbarn erkunden
        for dx, dy in directions:
            neighbor = (current_pos[0] + dx, current_pos[1] + dy)

            # Überspringen, wenn Nachbar außerhalb der Karte oder blockiert ist
            if neighbor not in map_data or map_data[neighbor] == '#':
                continue

            # Neue Distanz berechnen
            new_distance = current_distance + 1

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor, path + [neighbor]))

    # Kein Pfad gefunden
    return []
