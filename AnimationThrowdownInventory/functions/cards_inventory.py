from read_cards import generate_cards_db
from consts import USER_FILE_PATH


def get_card_inventory():
    rarity_name = ["C", "R", "E", "L", "M"]

    card_catalog, my_cards = generate_cards_db(USER_FILE_PATH)

    my_inventory = {}
    for card in my_cards:
        rarity = rarity_name[int(card_catalog[card.unit_id].rarity) - 1]
        card_name = card_catalog[card.unit_id].name
        list_entry = f"{rarity}-{card.level}"

        if card_name not in my_inventory:
            my_inventory[card_name] = [list_entry]
        else:
            my_inventory[card_name].append(list_entry)
            my_inventory[card_name].sort(reverse=True)

    sorted_inventory = dict(sorted(my_inventory.items()))
    _generate_card_inventory_file(sorted_inventory)
    return sorted_inventory


def _generate_card_inventory_file(card_inventory: dict):
    with open("output/cards-inventory.txt", "w") as f:
        for card_name, card_list in card_inventory.items():
            f.write(f"{card_name:30}: {' '.join(card_list)}\n")
