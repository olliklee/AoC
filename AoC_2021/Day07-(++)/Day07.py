# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2021", "07"

def solve():
  riddles = list(map(int, load_input(delimiter=',')))

  fuels_a = []
  fuels_b = []
  for destination in range(max(riddles) + 1):
      fuel_a = fuel_b = 0
      for riddle in riddles:
          fuel_a += abs(riddle - destination)

          distance = abs(riddle - destination)
          for consumption in range(1, distance + 1):
              fuel_b += consumption

      fuels_a.append(fuel_a)
      fuels_b.append(fuel_b)


  part_a = min(fuels_a)
  part_b = min(fuels_b)

  return part_a, part_b


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
