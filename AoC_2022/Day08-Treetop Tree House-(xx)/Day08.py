# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2022", "08"

forest = load_input(split_by_line=True)
dim_x = len(forest[0])
dim_y = len(forest)


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
    while True:
        x += dx
        y += dy
        if x < 0 or x >= dim_x or y < 0 or y >= dim_y:
            break
        next_tree = int(forest[x][y])
        seen_trees += 1
        if next_tree >= treehouse:
            break
    return seen_trees


def look_up(x, y):
    return look_direction(x, y, -1, 0)


def look_down(x, y):
    return look_direction(x, y, 1, 0)


def look_left(x, y):
    return look_direction(x, y, 0, -1)


def look_right(x, y):
    return look_direction(x, y, 0, 1)


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
    
    max_score = 0
    for col in range(dim_x):
        for row in range(dim_y):
            score = look_up(col, row) * look_down(col, row) * look_right(col, row) * look_left(col, row)
            max_score = max(score, max_score)
    
    part2 = max_score

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day,year,solve)
