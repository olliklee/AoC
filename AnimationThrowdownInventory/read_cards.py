import json
from pathlib import Path
from typing import List, Dict, Tuple
from cards import Card, MyCard


class CardDataProcessor:
    def __init__(self, input_file: str, output_file: str = "output/card_catalog-w-id-and-rarity.txt"):
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)
        self.card_catalog: Dict[str, Card] = {}
        self.my_cards: List[MyCard] = []

    def load_card_data(self) -> Dict:
        """Load and parse JSON card data from input file."""
        with open(self.input_file) as f:
            return json.load(f)['card_data']

    def load_my_card_data(self) -> Dict:
        """Load and parse JSON card data from input file."""
        with open(self.input_file) as f:
            return json.load(f)['user_units']

    def process_cards(self):
        """Process card data and return formatted lines."""
        card_data = self.load_card_data()
        my_card_data = self.load_my_card_data()

        for card_id, card_info in card_data.items():
            card = Card.from_dict(card_id, card_info)
            self.card_catalog[card_id] = card

        for card_id, card_info in my_card_data.items():
            my_card = MyCard.from_dict(card_id, card_info)
            self.my_cards.append(my_card)

    def get_all_cards(self):
        return self.card_catalog

    def get_my_cards(self):
        return self.my_cards


def generate_cards_db(input_file: str) -> Tuple[dict[str, Card], list[MyCard]]:
    """Main function to generate card_catalog file."""
    processor = CardDataProcessor(input_file)
    processor.process_cards()
    all_cards = processor.get_all_cards()
    my_cards = processor.get_my_cards()
    return all_cards, my_cards
