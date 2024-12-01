# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

from dijkstar import Graph, find_path
import networkx as nx


year, day = "2023", "17"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = test              # change to final when ready


def prepare_input():
    with open(filename) as f:
        content = f.read().split("\n")

    return content


def solve_a():
    startx, starty, endx, endy = 0, 0, xmax - 1, ymax - 1
    graph = Graph()
    graph.add_edge((0,0), (1,0), 4)
    graph.add_edge((0,0), (2,0), 1)
    graph.add_edge((0,0), (3,0), 3)
    find_path(graph,(0,0), (3,0))

    # code goes here
    return 0


def solve_b():
    # code goes here
    return 0

### ----------- Start ------------- ###

puzzle = prepare_input()

xmax = len(puzzle[0])
ymax = len(puzzle)

run_puzzles(day, year, solve_a, solve_b)
