import json
from classes import Deck, Card

from consts import USER_FILE_PATH, JS_USER_DECKS


def get_decks_inventory():
    with open(f'../{USER_FILE_PATH}') as f:
        data = json.load(f)[JS_USER_DECKS]

    for deck_id, deck_info in data.items():
        deck = Deck.from_dict(deck_id, deck_info)
        print(deck.name, deck.hero_level)


get_decks_inventory()
