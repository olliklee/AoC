# # #  Solutions of Advent of Code
# # #  Oliver Kleemann


from aoc_helper import *
import re

year, day = '2024', '17'

xxx = '''
The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
'''


def parse(com: int, operand: int, register, pointer:int, result: list):
  a, b, c = register
  combo_op = combo(operand, register)
  
  match com:
    case 0: a //= 2 ** combo_op
    case 1: b ^= operand
    case 2: b = combo_op & 7
    case 3: pointer = operand if a else pointer + 2
    case 4: b ^= c
    case 5: result.append(str(combo_op % 8))
    case 6: b = a // 2 ** combo_op
    case 7: c = a // 2 ** combo_op
  
  if com != 3: pointer += 2
  
  return (a, b, c), pointer


def combo(operand, register):
  a, b, c = register
  match operand:
    case 0 | 1 | 2 | 3: return operand
    case 4: return a
    case 5: return b
    case 6: return c
    case _: return None


def solve():
  part2 = 0
  registers, program = load_input(test=0).split('\n\n')
  
  registers = list(map(int, re.findall(r'(\d+)', registers)))
  program = list(map(int, program[9:].split(',')))
  
  output = []
  pointer = 0
  while pointer < len(program)-1:
    com, op = program[pointer], program[pointer + 1]
    registers, pointer = parse(com, op, registers, pointer, output)
  part1 = ','.join(output)
  
  new_code = []
  reg_a = 66171486
  while new_code != program:
    reg_a += 1
    output = []
    pointer = 0
    while pointer < len(program) - 1:
      com, op = program[pointer], program[pointer + 1]
      registers, pointer = parse(com, op, (reg_a, 0, 0), pointer, output)
    print(output)
    
    print('\b\b\b\b\b\b\b\b' + str(reg_a), end='')
  print(registers)
  
  
  return part1, part2


### ----------- Start ------------- ###

run_puzzle(day, year, solve)


#falsch 6,3,5,5,1,6,1,5,1