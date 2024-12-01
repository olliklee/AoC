# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

import sys

year, day = "2023", "16"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final  # change to final when ready

DIR = {0: (0, -1), 90: (+1, 0), 180: (0, +1), 270: (-1, 0)}
energized = set()

sys.setrecursionlimit(5000)

def prepare_input():
    with open(filename) as f:
        content = f.read().split("\n")

    return content


def handle_mirror(angle: int, x: int, y: int):
    """ This function calculates the new angle and directions for a given position and direction.
    :param angle: integer (0,90,180,270)
    :param x: integer actual field x coordinate
    :param y: integer actual field x coordinate
    :return: None (Light beams out of field)
    :return: tuple (angle, x, y) (Light beam follows a single direction
    :return: tuple (angle1, x1, y1, angle2, x2, y2) (Light beam hitted a splitter)
    """
    sign = puzzle[y][x]
    new_ang1 = new_ang2 = new_x1 = new_y1 = new_x2 = new_y2 = None
    if sign == "/":
        new_ang1 = (angle + (90 if angle in [0, 180] else -90)) % 360
        new_x1, new_y1 = x + DIR[new_ang1][0], y + DIR[new_ang1][1]

    elif sign == "\\":
        new_ang1 = (angle + (90 if angle in [90, 270] else -90)) % 360
        new_x1, new_y1 = x + DIR[new_ang1][0], y + DIR[new_ang1][1]

    elif sign == "-":
        if angle in [90, 270]:
            new_ang1 = angle
            new_x1, new_y1 = x + DIR[angle][0], y + DIR[angle][1]

        elif angle in [180, 0]:
            new_ang1, new_ang2 = 90, 270
            new_x1, new_y1 = x + DIR[90][0], y + DIR[90][1]
            new_x2, new_y2 = x + DIR[270][0], y + DIR[270][1]

    elif sign == "|":
        if angle in [0, 180]:
            new_ang1 = angle
            new_x1, new_y1 = x + DIR[angle][0], y + DIR[angle][1]

        elif angle in [90, 270]:
            new_ang1, new_ang2 = 0, 180
            new_x1, new_y1 = x + DIR[new_ang1][0], y + DIR[new_ang1][1]
            new_x2, new_y2 = x + DIR[new_ang2][0], y + DIR[new_ang2][1]
    else:
        new_ang1 = angle
        new_x1, new_y1 = x + DIR[angle][0], y + DIR[angle][1]

    # checks boundaries
    result1 = result2 = None
    if new_ang1 is not None:
        if 0 <= new_x1 < xmax and 0 <= new_y1 < ymax:
            result1 = (new_ang1, new_x1, new_y1)
    if new_ang2 is not None:
        if 0 <= new_x2 < xmax and 0 <= new_y2 < ymax:
            result2 = (new_ang2, new_x2, new_y2)

    # calculates the return value
    if result1 and not result2:
        return new_ang1, new_x1, new_y1
    elif not result1 and result2:
        return new_ang2, new_x2, new_y2
    elif result1 and result2:
        return result1 + result2
    else:
        return None


def light_beam(angle: int, x: int, y: int):
    """ This recursive function takes the direction angle, x, y of
    the light beam as parameters.
    It checks the content of the actual field and reacts on mirrors and splitters
    and calls itself with the new direction of the beam """

    # if the light beam is on a former track -> stop the function
    # to avoid following a circle
    if (angle, x, y) in energized:
        return 0
    # add the trackpoint to the energized fields
    energized.add((angle, x, y))

    # Check if a mirror or splitter is on the actual field
    # If the handle_mirrors gives no valid results back, the beam has left the map.
    tuple_returned = handle_mirror(angle, x, y)
    if tuple_returned is not None:
        if len(tuple_returned) == 3:
            light_beam(*tuple_returned[:3])
        elif len(tuple_returned) == 6:
            light_beam(*tuple_returned[:3])
            light_beam(*tuple_returned[3:])
    else:
        return 0


def solve_a():
    light_beam(90, 0, 0)

    return len(set((x, y) for _, x, y in energized))


def solve_b():
    max_energized = 0
    # all fields in top and bottom row as beam starter
    for x in range(xmax):
        energized.clear()
        light_beam(180, x, 0)
        max_energized = max(len(set((x, y) for _, x, y in energized)), max_energized)

        energized.clear()
        light_beam(0, x, ymax - 1)
        max_energized = max(len(set((x, y) for _, x, y in energized)), max_energized)

    # all fields in left and right column as beam starter
    for y in range(ymax):
        energized.clear()
        light_beam(0, 0, y)
        max_energized = max(len(set((x, y) for _, x, y in energized)), max_energized)

        energized.clear()
        light_beam(270, xmax - 1, y)
        max_energized = max(len(set((x, y) for _, x, y in energized)), max_energized)

    return max_energized


### ----------- Start ------------- ###

puzzle = prepare_input()

xmax = len(puzzle[0])
ymax = len(puzzle)

run_puzzles(day, year, solve_a, solve_b)
