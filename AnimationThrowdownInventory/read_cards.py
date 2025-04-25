import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Optional


@dataclass
class Card:
    card_id: str
    card_name: str
    card_rarity: str
    card_type: str
    card_health: str
    card_attack: str
    card_power: str
    card_cardtype: str
    card_trait: List[str]
    card_skill: List[str]
    card_upgrade: List[Dict]

    @classmethod
    def from_dict(cls, card_id: str, card_info: Dict) -> 'Card':
        return cls(
            card_id=card_id,
            card_name=card_info.get('name', ''),
            card_rarity=card_info.get('rarity', ''),
            card_type=card_info.get('type', ''),
            card_health=card_info.get('health', ''),
            card_attack=card_info.get('attack', ''),
            card_power=card_info.get('power', ''),
            card_cardtype=card_info.get('card_type', ''),
            card_trait=card_info.get('trait', []),
            card_skill=card_info.get('skill', []),
            card_upgrade=card_info.get('upgrade', [])
        )

    def format_line(self) -> Optional[str]:
        """Format card information as a string line if name and rarity exist."""
        if self.card_name and self.card_rarity:
            return f"{self.card_id:7} {self.card_rarity} {self.card_name}"
        return None


class CardDataProcessor:
    def __init__(self, input_file: str, output_file: str = "output/cards-w-id-and-rarity.txt"):
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)
        self.cards: List[Card] = []

    def load_card_data(self) -> Dict:
        """Load and parse JSON card data from input file."""
        with open(self.input_file) as f:
            return json.load(f)['card_data']

    def process_cards(self) -> List[str]:
        """Process card data and return formatted lines."""
        card_data = self.load_card_data()
        formatted_lines = []

        for card_id, card_info in card_data.items():
            card = Card.from_dict(card_id, card_info)
            self.cards.append(card)

            if formatted_line := card.format_line():
                formatted_lines.append(formatted_line)

        return sorted(set(formatted_lines))

    def save_to_file(self, formatted_lines: List[str]) -> None:
        """Save formatted lines to output file."""
        self.output_file.parent.mkdir(exist_ok=True)
        with open(self.output_file, "w") as f:
            f.write("\n".join(formatted_lines) + "\n")
        print(f"wrote {self.output_file}")


def generate_cards_file(input_file: str) -> None:
    """Main function to generate cards file."""
    processor = CardDataProcessor(input_file)
    formatted_lines = processor.process_cards()
    processor.save_to_file(formatted_lines)