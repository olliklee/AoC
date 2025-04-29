import json
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from consts import JS_CARDS, JS_USER_CARDS


@dataclass
class Card:
    card_id: str
    name: str
    rarity: str
    show: str
    health: str
    attack: str
    power: str
    cardtype: str  # object, character, final_form
    trait: List[str]
    skill: List[str]
    upgrade: List[Dict]
    attack_multiplier: str
    health_multiplier: str

    @classmethod
    def from_dict(cls, card_id: str, card_info: Dict) -> 'Card':
        return cls(
            card_id=card_id,
            name=card_info.get('name', '').replace("'", "\'"),
            rarity=card_info.get('rarity', ''),
            show=card_info.get('type', ''),
            health=card_info.get('health', ''),
            attack=card_info.get('attack', ''),
            power=card_info.get('power', ''),
            cardtype=card_info.get('card_type', ''),
            trait=card_info.get('trait', []),
            skill=card_info.get('skill', []),
            upgrade=card_info.get('upgrade', []),
            attack_multiplier=card_info.get('attack_multiplier', '0'),
            health_multiplier=card_info.get('health_multiplier', '0'),
        )


    def format_w_id_and_rarity(self) -> Optional[str]:
        """Format card information as a string line if name and rarity exist."""
        if self.name and self.rarity:
            return f"{self.card_id:7} {self.rarity} {self.name}"
        return None


@dataclass
class CardsDB:
    cards: Dict[str, Card]

    @classmethod
    def from_user_file(cls, user_file):
        # Datei öffnen und JSON-Inhalt laden
        with open(user_file) as f:
            data = json.load(f)
            all_cards = data[JS_CARDS]  # JS_CARDS Konstante verwenden

        cards = {}
        for card_id, card_info in all_cards.items():
            card = Card.from_dict(card_id, card_info)
            cards[card_id] = card

        return cls(cards=cards)

    def get_card(self, card_id: str) -> Optional[Card]:
        return self.cards.get(card_id)
    

@dataclass
class MyCard:
    card_id: str
    unit_id: str
    level: str
    max_level: str
    power: str
    mastery_level: str
    mastery_current_attack: str
    mastery_current_health: str
    mastery_current_skills: List[Dict]

    @classmethod
    def from_dict(cls, card_id: str, card_info: Dict) -> 'MyCard':
        return cls(
            card_id=card_id,
            unit_id=card_info.get('unit_id', ''),
            level=card_info.get('level', ''),
            max_level=card_info.get('max_level', ''),
            power=card_info.get('power', '0'),
            mastery_level=card_info.get('mastery_level', ''),
            mastery_current_attack=card_info.get('mastery_current_attack', ''),
            mastery_current_health=card_info.get('mastery_current_health', ''),
            mastery_current_skills=card_info.get('mastery_current_skills', []),
        )


@dataclass
class MyCardsDB:
    cards: List[MyCard]
    card_db: CardsDB

    @classmethod
    def from_user_file(cls, user_file: str, card_db: CardsDB):
        # Datei öffnen und JSON-Inhalt laden
        with open(user_file) as f:
            data = json.load(f)
            my_cards_data = data[JS_USER_CARDS]  # Konstante für user_cards

        # MyCard Objekte erstellen
        my_cards = []
        for card_id, card_info in my_cards_data.items():
            my_card = MyCard.from_dict(card_id, card_info)
            my_cards.append(my_card)

        return cls(cards=my_cards, card_db=card_db)

    def get_card_info(self, my_card: MyCard) -> Optional[Card]:
        """Gibt die zugehörige Card-Information aus der CardDB zurück."""
        return self.card_db.get_card(my_card.unit_id)

    def get_all_cards_with_info(self) -> List[Tuple[MyCard, Optional[Card]]]:
        """Gibt eine Liste von Tupeln mit MyCard und zugehöriger Card zurück."""
        return [(my_card, self.get_card_info(my_card)) for my_card in self.cards]

    def print_cards_inventory(self):
        """Druckt eine formatierte Übersicht aller Karten."""
        for my_card, card_info in self.get_all_cards_with_info():
            if card_info:
                print(f"Level {my_card.level} {card_info.name} ({card_info.rarity}) - Power: {my_card.power}")
            else:
                print(f"Unbekannte Karte: ID {my_card.unit_id} - Level {my_card.level}")


@dataclass()
class Deck:
    deck_id: str
    name: str
    hero_id: str
    hero_level: str
    cards: List[MyCard]

    @classmethod
    def from_dict(cls, deck_id: str, deck_info: Dict) -> 'Deck':
        return cls(
            deck_id=deck_id,
            name=deck_info.get('name', '').replace("'", "\'"),
            hero_id=deck_info.get('commander', {}).get('unit_id'),
            hero_level=deck_info.get('commander', {}).get('level'),
            cards=[MyCard.from_dict(unit.get('card_id', ''), unit) for unit in deck_info.get('units', [])]
        )
