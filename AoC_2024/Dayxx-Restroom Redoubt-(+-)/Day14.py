# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re


year, day = '2024', '14'


def calc_pos(robot, steps, dimx, dimy):
  x, y, vx, vy = robot
  newx, newy = (x + steps * vx) % dimx, (y + steps * vy) % dimy
  return newx, newy


def get_quarter(pos, dimx, dimy):
  x, y = pos
  size_x, size_y =  dimx // 2, dimy // 2

  if x < size_x and y < size_y: return 1
  elif x < size_x and y > size_y: return 2
  elif x > size_x and y < size_y: return 3
  elif x > size_x and y > size_y: return 4
  else: return 0


def print_map(positions, dimx, dimy):
  matrix = ''
  for y in range(dimy):
    line = ''
    for x in range(dimx):
      if (x, y) in positions:
        line += '0'
      else:
        line += '.'
    
    matrix += line + "\n"

    print(matrix)


def solve():
  part1 = part2 = 0
  dimx, dimy = 101, 103
  testmode = False
  if testmode:
    dimx, dimy = 11, 7
    steps = 100

  puzzle = load_input(day, test=testmode)
  robots = re.findall(r'(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', puzzle, re.MULTILINE)
  robot_count = len(robots)
  for step in range(dimx * dimy):

    pos_lst = []
    pos_set = set()
    for robot in robots:
      robot = list(map(int, robot))
      if step == 100:
        pos_lst.append(calc_pos(robot, step, dimx, dimy))
      
      pos_set.add(calc_pos(robot, step, dimx, dimy))
    
    if step == 100:
      counter = [get_quarter(pos, dimx, dimy) for pos in pos_lst]
      part1 = counter.count(1) * counter.count(2) * counter.count(3) * counter.count(4)

    if len(pos_set) == robot_count:
      part2 = step
        #print_map(positions,dimx,dimy)
      
    if part1 and part2:
      break
  
  return part1, part2

### ----------- Start ------------- ###

run_puzzle(day, year, solve)
