# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2021", "03"

class Card:
    def __init__(self):
        self.numbers = [0] * 25
        self.bingo = False
        self.lucky_number_when_bingo = -1
        self.rank = 0

    def __str__(self):
        result = ""
        for i in range(5):
            for j in range(5):
                result += f"{self.numbers[i * 5 + j]:3} "
            result += "\n"
        return result

    def mark_number(self, lucky_number):
        if not self.bingo:  # Karte hatte noch keinen Bingo
            for i, number in enumerate(self.numbers):
                if number == lucky_number:
                    self.numbers[i] += 500

    def check_for_bingo(self, lucky_number):
        if not self.bingo:  # Karte hatte noch keinen Bingo
            sums = []
            for i in range(5):
                sums.append(sum(self.numbers[i * 5: (i * 5) + 5]))  # Reihe summiert
                sums.append(sum(self.numbers[i:: 5]))  # Spalte summiert

            if max(sums) > 2500:  # Bingo, wenn Reihe oder Spalte addiert über 500 ergibt
                self.bingo = True
                self.lucky_number_when_bingo = lucky_number

    def get_sum_of_unmarked_fields(self):
        return sum([number for number in self.numbers if number < 500])


def read_input_from_file():

    return load_input().split('\n')


def read_drawn_numbers(data_from_file):
    drawn_numbers = data_from_file[0].split(",")
    drawn_numbers_int = [int(number) for number in drawn_numbers]
    del data_from_file[0:2]  # Lösche unrelevante Daten
    return drawn_numbers_int


def read_card_data(lines):
    card_data = []
    for line in lines:
        if len(line) != 0:
            splitted_line = line.split()
            for number in splitted_line:
                card_data.append(int(number))
    return card_data


def create_cards(card_data):
    cards = []
    number_of_cards = int(len(card_data) / 25)
    for i in range(number_of_cards):
        cards.append(Card())
        cards[i].numbers = card_data[i * 25: i * 25 + 25]
    return cards


def solve_a():
    data = read_input_from_file()
    drawn_numbers = read_drawn_numbers(data)
    card_data = read_card_data(data)
    cards = create_cards(card_data)

    for lucky_number in drawn_numbers:
        for card in cards:
            card.mark_number(lucky_number)
            card.check_for_bingo(lucky_number)
            if card.bingo:
                return lucky_number * card.get_sum_of_unmarked_fields()


def solve_b():
    data = read_input_from_file()
    drawn_numbers = read_drawn_numbers(data)
    card_data = read_card_data(data)
    cards = create_cards(card_data)
    winning_cards = []
    rank_counter = 1

    for lucky_number in drawn_numbers:
        for card in cards:
            card.mark_number(lucky_number)
            card.check_for_bingo(lucky_number)
            if card.bingo and card.rank == 0:
                card.rank = rank_counter
                rank_counter += 1
                winning_cards.append(card)
    last_win_card = winning_cards[-1]

    return last_win_card.lucky_number_when_bingo * last_win_card.get_sum_of_unmarked_fields()


### ----------- Start ------------- ###

run_puzzles(day, year, solve_a, solve_b)
