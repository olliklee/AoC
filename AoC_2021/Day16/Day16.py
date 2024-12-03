# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2024", "03"

def destructure(hex_num: str) -> str:
  version, type_id = hex_num[0:3], hex_num[3:6]
  if int(type_id) == 4:
    print('literal')

def solve():
  bits = ''.join([bin(int(digit, 16))[2:] for digit in load_input()])

  offset = 0
  while len(bits) > (0 + offset):
    version, type_id = bits[0:3], bits[3:6]



  result_a = result_b = 0
  return result_a, result_b


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
