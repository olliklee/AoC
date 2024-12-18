# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

from collections import defaultdict

year, day = "2023", "15"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final  # change to final when ready


def prepare_input():
    with open(filename) as f:
        content = f.read().split(",")

    return content


def to_hash(text: str = "HASH") -> int:
    result = 0
    for letter in text:
        result = ((result + ord(letter)) * 17) % 256
    return result


def solve_a():
    return sum(to_hash(word) for word in puzzle)


def solve_b():
    # Lösung von Gravitar https://www.youtube.com/watch?v=RfycgXHphsg&t=83s
    # Ehrlich gesagt habe ich den zweiten Teil nicht mal verstanden...
    boxes = defaultdict(dict)
    for lens in puzzle:
        if "=" in lens:
            name, foc = lens.split("=")
            boxes[to_hash(name)][name] = int(foc)
        else:
            name = lens[:-1]
            boxes[to_hash(name)].pop(name, None)

    return sum((box + 1) * lensnr * foc
               for box, lense in boxes.items()
               for lensnr, foc in enumerate(lense.values(), start=1))


#  ----------   Start   ----------   #

puzzle = prepare_input()

run_puzzles(day, year, solve_a, solve_b)
