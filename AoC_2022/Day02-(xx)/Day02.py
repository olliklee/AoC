#  Solutions of Advent of Code
#  Oliver Kleemann

from AoC_2022.aoc_helper import run

year, day = "2022", "02"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final

def prepare_input(file_name):
    with open(file_name) as f:
        game = []
        for line in f:
            line = line.strip().split()
            game.append((line[0], line[1]))
    return game


def solve_a():
    game = prepare_input(f"Day{day}_input.txt")
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

    return total_score


def solve_b():
    game = prepare_input(f"Day{day}_input.txt")
    elves_choice = "ABC"  # rock, paper, scissor
    my_option = "XYZ"  # lose, draw, win
    total_score = 0
    for my_round in game:
        win_score = my_option.index(my_round[1]) * 3
        my_choice_score = (elves_choice.index(my_round[0]) + (my_option.index(my_round[1]) + 2) % 3) % 3 + 1
        total_score += win_score + my_choice_score

    return total_score


game = prepare_input(filename)

run(day, year, solve_a, solve_b)
