# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2024", "06"


def find_start(maze):
    for y, line in enumerate(maze):
        if '^' in line:
            return line.index('^'), y, 0


def obstacle_ahead(maze, x, y, direction):
    x_next, y_next = forward(x, y, direction)
    return maze[y_next][x_next] in '#O'


def out_of_bounds(maze, x, y, direction):
    x_next, y_next = forward(x, y, direction)
    return x_next < 0 or x_next >= len(maze[0]) or y_next < 0 or y_next >= len(maze)


def forward(x, y, direction):
    if direction == 0:
        return x, y - 1
    elif direction == 180:
        return x, y + 1
    elif direction == 90:
        return x + 1, y
    elif direction == 270:
        return x - 1, y


def turn(direction):
    return (direction + 90) % 360


def solve():
    puzzle = [list(line) for line in load_input(test=False, split_by_line=True)]
    puzzle_origin = puzzle[:]

    marked = set()
    start_x, start_y, direction = find_start(puzzle)
    x, y = start_x, start_y

    # part 1
    while not out_of_bounds(puzzle, x, y, direction):

        while obstacle_ahead(puzzle, x, y, direction):
            direction = turn(direction)

        x, y = forward(x, y, direction)
        marked.add((x, y))

    # part 2
    num_of_loops = 0
    walked_over = dict()

    for key in marked:
        # pass start field
        if key == (start_x, start_y):
            continue

        # reset Maze
        x, y, direction = find_start(puzzle)
        puzzle = puzzle_origin
        walked_over.clear()

        # set new obstacle
        new_obstacle = key
        puzzle[new_obstacle[1]][new_obstacle[0]] = 'O'

        while not out_of_bounds(puzzle, x, y, direction):
            while obstacle_ahead(puzzle, x, y, direction):
                direction = turn(direction)

            x, y = forward(x, y, direction)
            if (x, y) in walked_over:
                if direction in walked_over[(x, y)]:
                    num_of_loops += 1
                    if num_of_loops % 100 == 0:
                        print(20 * '\b' + 6 * ' ' + f'Found: {num_of_loops}', end='')
                    break
                else:
                    walked_over[(x, y)].add(direction)
            else:
                walked_over[(x, y)] = {direction}

        # delete new obstacle
        puzzle[new_obstacle[1]][new_obstacle[0]] = '.'

    part1 = len(marked)
    part2 = num_of_loops

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
