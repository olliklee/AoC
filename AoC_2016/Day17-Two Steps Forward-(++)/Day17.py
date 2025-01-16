# # #  Solutions of Advent of Code
# # #  Oliver Kleemann
# # #  and a lot chatgpt

from aoc_helper import *
from hashlib import md5

year, day = "2016", "17"


def get_open_doors(password, position):
    directions = ['U', 'D', 'L', 'R']
    hash_value = md5(password.encode()).hexdigest()[:4]
    open_doors = [(direction, hash_value[i] in 'bcdef') for i, direction in enumerate(directions)]
    return open_doors


def is_valid_move(position, direction):
    x, y = position
    if direction == 'U' and x > 0:
        return True
    if direction == 'D' and x < 3:
        return True
    if direction == 'L' and y > 0:
        return True
    if direction == 'R' and y < 3:
        return True
    return False


def move_position(position, direction):
    x, y = position
    if direction == 'U':
        return x - 1, y
    if direction == 'D':
        return x + 1, y
    if direction == 'L':
        return x, y - 1
    if direction == 'R':
        return x, y + 1
    return position


def dfs_maze(password, start=(0, 0), goal=(3, 3)):
    stack = [(start, password, "")]
    paths = []
    
    while stack:
        position, current_password, path = stack.pop()
        
        if position == goal:
            paths.append(path)
            continue
        
        open_doors = get_open_doors(current_password, position)
        for direction, is_open in open_doors:
            if is_open and is_valid_move(position, direction):
                new_position = move_position(position, direction)
                stack.append((new_position, current_password + direction, path + direction))
    
    return paths


def solve():
    puzzle = 'lpvhkcbi'
    start, goal = (0, 0), (3, 3)
    paths = dfs_maze(puzzle, start, goal)
    
    part1 = min(paths, key=len)
    part2 = len(max(paths, key=len))
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
