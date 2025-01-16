# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import heapq

year, day = "2016", "13"


def is_wall(x, y, size):
    res = x * x + 3 * x + 2 * x * y + y + y * y + size
    return bin(res).count("1") % 2


def dijkstra(start, goal, size, max_steps):
    rows = cols = size
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    queue = [(0, start)]
    reached = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current_dist, (row, col) = heapq.heappop(queue)
        if (row, col) == goal:
            return current_dist, len(reached)
        if current_dist <= max_steps:
            reached.add((row, col))

        for dx, dy in directions:
            next_row, next_col = row + dy, col + dx
            if rows > next_row >= 0 == is_wall(next_row, next_col, size) and 0 <= next_col < cols:
                new_dist = current_dist + 1
                if new_dist < distances[next_row][next_col]:
                    distances[next_row][next_col] = new_dist
                    heapq.heappush(queue, (new_dist, (next_row, next_col)))
    return -1


def solve():
    size = 1350
    start, goal = (1, 1), (31, 39)

    part1, part2 = dijkstra(start, goal, size, 50)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
