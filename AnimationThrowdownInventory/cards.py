from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Card:
    card_id: str
    name: str
    rarity: str
    show: str
    health: str
    attack: str
    power: str
    cardtype: str  #object, character, final_form
    trait: List[str]
    skill: List[str]
    upgrade: List[Dict]
    attack_multiplier: str
    health_multiplier: str

    @classmethod
    def from_dict(cls, card_id: str, card_info: Dict) -> 'Card':
        return cls(
            card_id=card_id,
            name=card_info.get('name', ''),
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
