# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = '2024', '15'


def get_next_pos(pos, direction):
  x, y = pos
  moves = {'v': (0, 1), '>': (1, 0), '<': (-1, 0), '^': (0, -1)}
  dx, dy = moves.get(direction, (0, 0))
  return x + dx, y + dy


def no_free_space(room, pos, direction):
  row = ''
  while True:
    pos = get_next_pos(pos, direction)
    row += room[pos]
    if room[pos] == '#': break
  return '.' not in row


def walk(room, pos, direction):
  new_pos = get_next_pos(pos, direction)
  tile = room[new_pos]
  
  if tile == '#':
    return pos
  if tile == 'O' and not push_crates(room, pos, direction):
    return pos
  
  room[pos] = '.'
  room[new_pos] = '@'
  return new_pos
  

def push_crates(room, pos, direction):
  next_pos = get_next_pos(pos, direction)
  
  if no_free_space(room, pos, direction):
    return False
  
  if room[next_pos] == '.':
    room[next_pos] = 'O'
    return True
  
  if room[next_pos] == 'O':
    if push_crates(room, next_pos, direction):
      room[next_pos] = 'O'
      return True
  
  return False


def solve():
  part1 = part2 = 0
  
  room, moves = load_input(test=False).split('\n\n')
  room = room.split('\n')
  room = {(x, y): room[y][x] for y in range(len(room)) for x in range(len(room[y]))}
  
  robot = next((k for k, v in room.items() if v == '@')) # find the robot
  moves = moves.replace('\n', '')
  
  for direction in moves:
    robot = walk(room, robot, direction)
    part1 = sum([100 * y + x for (x, y), v in room.items() if v == 'O'])
  
  #print_matrix(room)
  
  return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
