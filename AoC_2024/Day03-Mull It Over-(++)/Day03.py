import re
 
with open('Day03_input.txt') as f:
  puzzle = f.read()

pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"

num_pattern = r'\d+'

lst = re.findall(pattern, puzzle)

result_a = result_b = 0
do = True
for command in lst:
  
  if command == 'do()':
    do = True
  
  if command == "don't()" :
    do = False

  if command[0:3] == 'mul':
    a,b = re.findall(num_pattern, command)
    mul = int(a) * int(b)
    result_a += mul
  
    if do:
      result_b += mul
    
  
print(result_a, result_b)