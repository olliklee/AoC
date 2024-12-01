# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter

year, day = "2022", "14"


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
        content = f.read()
        lines = content.split("\n")

    return lines


class Grain:
    def __init__(self, x, y, bottom):
        self.x = x
        self.y = y
        self.floor = bottom

    def fall(self):
        if self.y >= self.floor:
            raise OverflowError

        next_p = self.x, self.y + 1
        left = self.x - 1, self.y + 1
        right = self.x + 1, self.y + 1
        if self.is_free(next_p):
            self.x, self.y = next_p
            self.fall()
        elif self.is_free(left):
            self.x, self.y = left
            self.fall()
        elif self.is_free(right):
            self.x, self.y = right
            self.fall()
        else:
            sand.add((self.x, self.y))
        if self.y == 0:
            raise OverflowError

        return True

    def is_free(self, point):
        x, y = point
        if (x, y) not in block and (x, y) not in sand:
            return True
        else:
            return False


def line_to_points(line: str):
    start, end = line.split(" -> ")
    x1, y1 = list(map(int, start.split(",")))
    x2, y2 = list(map(int, end.split(",")))
    delta_x, delta_y = x2 - x1, y2 - y1

    if delta_x < 0 or delta_y < 0:
        step = -1
    else:
        step = 1

    if delta_x != 0:
        for x in range(x1, x2, step):
            block.add((x, y1))
    elif delta_y != 0:
        for y in range(y1, y2, step):
            block.add((x1, y))
    block.add((x2, y2))


def make_walls():
    blocking_structure = prepare_input(f"/Volumes/Programmieren/PythonProjects/AdventOfCode/AoC 2022/input/Day14_input.txt")
    block.clear()
    sand.clear()
    for line in blocking_structure:
        points = line.split(" -> ")
        for i in range(len(points) - 1):
            line_to_points(points[i] + " -> " + points[i + 1])


def sand_fall(bottom) -> int:
    counter = 0
    while True:
        korn = Grain(500, 0, bottom)
        try:
            korn.fall()
            counter += 1
        except OverflowError:
            return counter


def solve_a():
    make_walls()
    bottom_line = max([y[1] for y in block])
    return sand_fall(bottom_line)


def solve_b():
    make_walls()
    bottom_line = max([y[1] for y in block]) + 2
    for x in range(-800, 800):
        block.add((x, bottom_line))

    return sand_fall(bottom_line)+1


block = set()
sand = set()

run(day, year)
