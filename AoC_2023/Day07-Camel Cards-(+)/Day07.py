# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

from collections import Counter

year, day = "2023", "07"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final

card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
# card_values2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

score_values = ['11111', '2111', '221', '311', '32', '41', '5']


def prepare_input(file_name: str) -> list:
    with open(file_name) as f:
        return [tuple(line.split()) for line in f.read().split("\n")]


def get_score(deck: str) -> int:
    """ takes the 5 caard deck as string and returns a kind of 'poker' score"""
    card = Counter(deck).most_common()
    print(card)  # the Counter is sorted by the highest amount of cards of same type
    analyzed = [card[i][1] for i in range(len(card))]
    return score_values.index("".join(list(map(str, analyzed)))) + 1


def get_sort_score(word: str) -> str:
    """ takes the 5 card deck as string and returns a sortable string """
    # generates a word suitable to sort after this
    # the score of each card can be higher than 10 so i used hex numbers
    return "".join([hex(card_values.index(letter))[2:] for letter in word])


def solve_a() -> int:
    result = 0
    # all decks sorted by the sort key: (sortkey, (deck, bet))
    sorted_list = sorted([(str(get_score(deck[0])) + str(get_sort_score(deck[0])), deck) for deck in puzzle],
                         key=lambda x: x[0])

    for index, deck in enumerate(sorted_list):
        # index+1 is the rank of the deck multiplicated with the bet
        result += (index + 1) * int(deck[1][1])

    return result


def solve_b() -> str:  # or int
    # something recursive... one day i understand how that goes
    return "not solved"


#  ----------   Start   ----------   #

puzzle = prepare_input(filename)
run_puzzles(day, year, solve_a, solve_b)
