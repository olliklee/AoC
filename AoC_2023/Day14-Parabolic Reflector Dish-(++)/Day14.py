# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

year, day = "2023", "14"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final  # change to final when ready


def prepare_input():
    with open(filename) as f:
        content = f.read().split("\n")
    return content


def roll_all(matrix):
    for r_ind in range(len(matrix)):
        if r_ind == 0:
            continue

        for c_ind in range(len(matrix[r_ind])):
            if matrix[r_ind][c_ind] == "O":
                roll_up(matrix, r_ind, c_ind)


def roll_up(matrix, row, col):
    if matrix[row - 1][col] in ("#", "O") or row == 0:
        return
    else:
        matrix[row] = matrix[row][0:col] + '.' + matrix[row][col + 1:]
        matrix[row - 1] = matrix[row - 1][0:col] + 'O' + matrix[row - 1][col + 1:]
        roll_up(matrix, row - 1, col)


def rotate_matrix(matrix):
    # Transpose the matrix
    transposed_matrix = list(zip(*matrix))

    # Reverse the order of rows
    rotated_matrix = ["".join(list(row)[::-1]) for row in transposed_matrix]

    return rotated_matrix


# def print_board(board):
#     for row in board:
#         print(row)
#     print("\n\n")
#

def solve_a():
    puzzle = prepare_input()
    roll_all(puzzle)

    multiplicator = len(puzzle)
    result = 0
    for row in puzzle:
        result += row.count("O") * multiplicator
        multiplicator -= 1

    return result


def solve_b():
    puzzle = prepare_input()
    for i in range(251):  # spätestens alle 250 drehungen kommt die Zahl vor
        for j in range(4):  # auch beim Test input. Das geht eleganter und schneller...
            roll_all(puzzle)
            puzzle = rotate_matrix(puzzle)

    multiplicator = len(puzzle)
    result = 0
    for row in puzzle:
        result += row.count("O") * multiplicator
        multiplicator -= 1

    return result


### ----------- Start ------------- ###

run_puzzles(day, year, solve_a, solve_b)
