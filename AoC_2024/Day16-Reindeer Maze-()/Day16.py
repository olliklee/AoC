# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = '2024', '16'

DIRECTIONS = {0: (0, -1), 90: (1, 0), 180: (0, 1), 270: (-1, 0)}


def forward(pos, direction):
  x, y = pos
  dx, dy = DIRECTIONS[direction]
  return x + dx, y + dy


def turn(left, direction):
  if left:
    return (direction - 90) % 360
  else:
    return (direction + 90) % 360


def run(maze, pos, direction, score, best_scores):
  # Prüfen, ob die Position außerhalb der Grenze ist oder blockiert wird
  if maze.get(pos) == '#' or (pos in best_scores and score >= best_scores[pos]):
    return None
  
  # Ziel gefunden: Rückgabe des Scores
  if maze.get(pos) == 'E':
    return score
  
  # Speichere den besten Score für die aktuelle Position
  best_scores[pos] = score
  
  # Initialisiere das Ergebnis mit None (kein gültiger Pfad)
  result = None
  
  # Bewegung vorwärts
  res = run(maze, forward(pos, direction), direction, score + 1, best_scores)
  if res is not None:
    result = min(result, res) if result is not None else res
  
  # Bewegung nach links
  new_dir = turn(True, direction)
  res = run(maze, forward(pos, new_dir), new_dir, score + 1001, best_scores)
  if res is not None:
    result = min(result, res) if result is not None else res
  
  # Bewegung nach rechts
  new_dir = turn(False, direction)
  res = run(maze, forward(pos, new_dir), new_dir, score + 1001, best_scores)
  if res is not None:
    result = min(result, res) if result is not None else res
  
  return result


def solve():
  part1 = part2 = 0
  
  puzzle = load_input(day, test=False)
  maze = text_to_dictmap(puzzle)
  start = next((pos for pos in maze if maze[pos] == 'S'))
  goal = next((pos for pos in maze if maze[pos] == 'E'))
  
  best_scores = {}
  part1 = run(maze, start, 0, 1000, best_scores)
  
  print(goal)
  print_matrix(maze)
  
  return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)

# 132588, 132589 too low
# 133588 too high
# 132589
