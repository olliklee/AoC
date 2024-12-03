# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2024", "03"
 
def solve():
  puzzle = load_input(test=False)

  pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
  num_pattern = r'\d+'
  commands = re.findall(pattern, puzzle)

  result_a = result_b = 0
  do = True
  for command in commands:

    if command == 'do()':
      do = True
    elif command == "don't()" :
      do = False
    elif command[0:3] == 'mul':
      a, b = re.findall(num_pattern, command)
      mul = int(a) * int(b)
      result_a += mul
      result_b += mul if do else 0

  return result_a, result_b
  
run_puzzle(day, year, solve)
