# # #  Solutions of Advent of Code
# # #  Oliver Kleemann (mit Hilfe von Gravitar Youtube)

from aoc_helper import *
year, day = "2022", "10"


def solve():
    program = [line.split() for line in load_input(split_by_line=True)]
    cycles = [20, 60, 100, 140, 180, 220]

    register = [1] + [value for com in program for value in ([0, int(com[1])] if com[0] != "noop" else [0])]
    
    part1 = sum([sum(register[:steps]) * steps for steps in cycles])
    
    # part 2
    register = 1
    reg = [1]
    for com in program:
        reg.append(register)
        if com[0] != "noop":
            reg.append(register)
            register += int(com[1])
    
    dsp = ""
    for step in range(0, 241):
        reg[step] += 1
        dsp += '\n' if not step % 40 else ' '
        dsp += '█' if (step % 40 - reg[step]) in [-1, 0, 1] else ' '

    print(dsp)
    part2 = 'BUCACBUZ'
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
