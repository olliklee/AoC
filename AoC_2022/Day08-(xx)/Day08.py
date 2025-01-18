# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter

year, day = "2022", "08"


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
        program = content.split("\n")

    return program


def solve_a():
    forest = prepare_input(f"Day{day}_input.txt")
    dim_x = len(forest[0])
    dim_y = len(forest)
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
    forest = prepare_input(f"Day{day}_input.txt")
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


run(day, year)
