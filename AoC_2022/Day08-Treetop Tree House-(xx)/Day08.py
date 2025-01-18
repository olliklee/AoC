# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2022", "08"

'''
3 0 3 7 3
2 5 5 1 2
6 5 3 3 2
3 3 5 4 9
3 5 3 9 0
'''


def is_visible(forest, pos, boundaries):
    if not pos in forest:
        return None
    
    x, y = pos
    height = forest[pos]
    max_x, max_y = boundaries
    
    if x == 0 or x == max_x or y == 0 or y == max_y:
        return True
    
    row_before = [forest[x, y] for x in range(x)]
    row_behind = [forest[x, y] for x in range(x + 1, max_x + 1)]
    col_before = [forest[x, y] for y in range(y)]
    col_behind = [forest[x, y] for y in range(y + 1, max_y + 1)]
    
    if any((max(row_before) < height, max(col_before) < height,
           max(row_behind) < height, max(col_behind) < height)):
        return True
    else:
        return False
        
        
def solve():
    part2 = 0
    puzzle = load_input(test=False)
    forest = text_to_dict_map(puzzle, int)
    boundaries = next(reversed(forest.keys()))
    visibles = set()
    for pos in forest.keys():
        if is_visible(forest, pos, boundaries):
            visibles.add(pos)
    part1 = len(visibles)

    return part1, part2


def solve_a():
    forest = load_input(split_by_line=True)
    dim_x, dim_y = len(forest[0]), len(forest)
    visible = set()
    
    # # Horizontal, L-R
    for i in range(dim_x):
        max_row = int(forest[i][0])
        visible.add((i, 0))
        for j in range(dim_y):
            tree = int(forest[i][j])
            if tree > max_row:
                max_row = tree
                visible.add((i, j))
    
    # # Horizontal, R-L
    for i in range(dim_y):
        max_row = int(forest[i][-1])
        visible.add((i, dim_y - 1))
        for j in range(dim_x - 1, -1, -1):
            tree = int(forest[i][j])
            if tree > max_row:
                max_row = tree
                visible.add((i, j))
    
    # Vertical, T-B
    for j in range(dim_y):
        maxtree = int(forest[0][j])
        visible.add((0, j))
        for i in range(dim_y):
            tree = int(forest[i][j])
            if tree > maxtree:
                maxtree = tree
                visible.add((i, j))
    
    for j in range(dim_y):
        maxtree = int(forest[-1][j])
        visible.add((dim_x - 1, j))
        for i in range(dim_x - 1, -1, -1):
            tree = int(forest[i][j])
            if tree > maxtree:
                maxtree = tree
                visible.add((i, j))
    
    return len(visible)


def solve_b():
    forest = load_input(split_by_line=True)
    dim_x = len(forest[0])
    dim_y = len(forest)
    max_score = 0
    
    def look_up(x, y):
        if y == 0:
            return 0
        treehouse = int(forest[x][y])
        seen_trees = 1
        while x - seen_trees > 0:
            next_tree = int(forest[x - seen_trees][y])
            if next_tree >= treehouse:
                break
            seen_trees += 1
        return seen_trees
    
    def look_down(x, y):
        if y == dim_y - 1:
            return 0
        treehouse = int(forest[x][y])
        seen_trees = 1
        while x + seen_trees < dim_x - 1:
            next_tree = int(forest[x + seen_trees][y])
            if next_tree >= treehouse:
                break
            seen_trees += 1
        return seen_trees
    
    def look_right(x, y):
        if x == dim_x - 1:
            return 0
        treehouse = int(forest[x][y])
        seen_trees = 1
        while y + seen_trees < dim_y - 1:
            next_tree = int(forest[x][y + seen_trees])
            if next_tree >= treehouse:
                break
            seen_trees += 1
        return seen_trees
    
    def look_left(x, y):
        if x == 0:
            return 0
        treehouse = int(forest[x][y])
        seen_trees = 1
        while y - seen_trees > 0:
            next_tree = int(forest[x][y - seen_trees])
            if next_tree >= treehouse:
                break
            seen_trees += 1
        return seen_trees
    
    for i in range(dim_x):
        for j in range(dim_y):
            score = look_up(i, j) * look_down(i, j) * look_right(i, j) * look_left(i, j)
            max_score = max(score, max_score)
    
    return max_score


#  ----------   Start   ----------   #

run_puzzle(day,year, solve)
run_puzzles(day,year,solve_a,solve_b)

'''
Results from AoC 2022 - Day 08
------------------------------
Day 08 - Part 1: 1700
Day 08 - Part 2: 470596

Performance
------------------------------
Part 1: 0.418767 ms
Part 2: 2.014296 ms
------------------------------
Gesamt: 2.433063 ms
'''
