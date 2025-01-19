# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2022", "08"

forest = load_input(split_by_line=True)
dim_x, dim_y = len(forest[0]), len(forest)


def scan_line(start, end, step, fixed, axis, visible):
    max_tree = float('-inf')
    for pos in range(start, end, step):
        x, y = (fixed, pos) if axis == 'horizontal' else (pos, fixed)
        tree = int(forest[x][y])
        if tree > max_tree:
            max_tree = tree
            visible.add((x, y))


def look_direction(x, y, dx, dy):
    treehouse = int(forest[x][y])
    seen_trees = 0
    while 0 <= x + dx < dim_x and 0 <= y + dy < dim_y:
        x += dx
        y += dy
        next_tree = int(forest[x][y])
        seen_trees += 1
        if next_tree >= treehouse:
            break
    return seen_trees


def solve():
    visible = set()
    
    # Horizontal scans
    for col in range(dim_x):
        scan_line(0, dim_y, 1, col, 'horizontal', visible)  # Left-to-right
        scan_line(dim_y - 1, -1, -1, col, 'horizontal', visible)  # Right-to-left
    
    # Vertical scans
    for row in range(dim_y):
        scan_line(0, dim_x, 1, row, 'vertical', visible)  # Top-to-bottom
        scan_line(dim_x - 1, -1, -1, row, 'vertical', visible)  # Bottom-to-top
    
    part1 = len(visible)
    
    max_score = max(
        look_direction(x, y, -1, 0) *  # Up
        look_direction(x, y, 1, 0) *   # Down
        look_direction(x, y, 0, 1) *   # Right
        look_direction(x, y, 0, -1)    # Left
        for x in range(dim_x) for y in range(dim_y)
    )

    part2 = max_score

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day,year,solve)
