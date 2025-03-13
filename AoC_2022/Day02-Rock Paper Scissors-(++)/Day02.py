#  Solutions of Advent of Code
#  Oliver Kleemann

from aoc_helper import *
import re

year, day = "2022", "02"


def solve():
    puzzle = load_input()
    game = re.findall(r'(\D) (\D)', puzzle)
    
    elves_choice = "ABC"  # rock, paper, scissor
    my_choice = "XYZ"  # rock, paper, scissor
    total_score = 0
    for my_round in game:
        opponent = elves_choice.index(my_round[0])
        me = my_choice.index(my_round[1])
        
        total_score += my_choice.index(my_round[1]) + 1  # score for chosen option
        if opponent == me:  # draw
            total_score += 3
        elif opponent == (me + 2) % 3:  # I win
            total_score += 6
    
    part1 = total_score
    
    elves_choice = "ABC"  # rock, paper, scissor
    my_option = "XYZ"  # lose, draw, win
    total_score = 0
    for my_round in game:
        win_score = my_option.index(my_round[1]) * 3
        my_choice_score = (elves_choice.index(my_round[0]) + (my_option.index(my_round[1]) + 2) % 3) % 3 + 1
        total_score += win_score + my_choice_score
    
    part2 = total_score
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
