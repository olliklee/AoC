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


def solved_by_gravitar():
  # damn that is so brillant
  part1 = part2 = 0
  p = load_input(test=False)

  enabled = True
  for dont, do, m1, m2 in re.findall(r'(don\'t\(\))|(do\(\))|mul\((\d+),(\d+)\)', p):
    if dont or do:
      enabled = do
      continue
    e = int(m1) * int(m2)
    part1 += e
    if not enabled: continue
    part2 += e

  return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)

print("From gravitar", end ='')
run_puzzle(day, year, solved_by_gravitar)