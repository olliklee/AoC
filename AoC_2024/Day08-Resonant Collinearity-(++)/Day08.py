# # #  Solutions of Advent of Code
# # #  Oliver Kleemann
from contextlib import nullcontext
from os import remove

from aoc_helper import *
from collections import defaultdict
from itertools import combinations

year, day = "2024", "08"


def get_antipode(point_a, point_b, grid):
  (x1, y1), (x2, y2) = point_a, point_b
  antipode = (point_b[0] - x1 + x2), (point_b[1] - y1 + y2)
  return antipode if antipode in grid else None


def get_all_antipodes(point_a, point_b, grid):
  all_nodes = set()
  all_nodes.add(point_a)
  all_nodes.add(point_b)
  while True:
    anti = get_antipode(point_a, point_b, grid)
    if anti:
      all_nodes.add(anti)
      point_a = point_b
      point_b = anti
    else:
      return all_nodes


def solve():
  content = load_input(test=True)
  puzzle = convert_to_dict_map(content)
  
  antennas = defaultdict(list)
  for spot in puzzle:
    loc = puzzle[spot]
    if loc not in '.#':
      antennas[loc].append(spot)
  
  nodes = set()
  for a_lst in antennas.values():
    for p1, p2 in combinations(a_lst, 2):
      node1 = get_antipode(p1, p2, puzzle)
      node2 = get_antipode(p2, p1, puzzle)
      nodes.add(node1)
      nodes.add(node2)
  if None in nodes:
    nodes.remove(None)
  
  part1 = len(nodes)
  
  for a_lst in antennas.values():
    combis = list(combinations(a_lst, 2))
    for a, b in combis:
      node_set1 = get_all_antipodes(a, b, puzzle)
      node_set2 = get_all_antipodes(b, a, puzzle)
      nodes.update(node_set1)
      nodes.update(node_set2)
  
  part2 = len(nodes)
  for node in nodes:
    puzzle[node] = '#'
  
  print_matrix(puzzle)
  return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)

# correct 1134
