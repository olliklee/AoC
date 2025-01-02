# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import run_puzzle

year, day = "2015", "10"


def look_and_say(number: str):
    number1 = number2 = 0
    for iterations in range(50):
        result = []
        count = 1
        prev = number[0]

        for i in range(1, len(number)):
            if number[i] == prev:
                count += 1
            else:
                # Speichere das Ergebnis in der Liste
                result.append(f"{count}{prev}")
                count = 1
                prev = number[i]

        # Letzten Abschnitt hinzufügen
        result.append(f"{count}{prev}")

        # Ergebnis als String für die nächste Iteration zusammenfügen
        number = ''.join(result)
        if iterations == 39:
            number1 = len(number)
        elif iterations == 49:
            number2 = len(number)

    return number1, number2


def solve():
    puzzle = '1113122113'

    part1, part2 = look_and_say(puzzle)

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
