# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

year, day = "2023", "01"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final

int_dict = {"one": 1, "two": 2, "three": 3,
            "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9,
            "zero": 0}


def prepare_input(file_name):
    with open(file_name) as f:
        content = f.read().split("\n")

    return content


def translate(text: str):
    new_text = ''
    # Goes letter by letter through the text string
    for index, letter in enumerate(text):
        # Letter is a digit? Add the letter to the translation string
        # skip the rest of the loop
        if letter.isdigit():
            new_text += letter
            continue

        # Goes through all entries of the dict if the following letters matches an entry
        for key in int_dict.keys():
            # Is the given index of the find method == the index from the enumeration?
            # if not just check the next int_dict entry
            if text.find(key, index) == index:
                # put the int from the dictionary into the translation string
                # and leave the dict iteration to get the next letter in the text string
                new_text += str(int_dict[key])
                break

    return new_text


def solve_a():
    sum_up = 0
    unwanted_chars = "abcdefghijklmnopqrstuvwxyz"

    for line in puzzle:
        # Remove all unnecessary letters from beginning and end
        new_line = line.strip(unwanted_chars)
        # first and last characters must now be digits
        # and can be concatenated, cast to int and added to the final sum
        sum_up += int(new_line[0] + new_line[-1])
    return sum_up


def solve_b():
    sum_up = 0
    for line in puzzle:
        new_line = translate(line)
        # first and last characters must now be digits
        # and can be concatenated, cast to int and added to the final sum
        sum_up += int(new_line[0] + new_line[-1])
    return sum_up


puzzle = prepare_input(filename)
run_puzzles(day, year, solve_a, solve_b)
