# https://github.com/toddhodes/AnimationThrowdown
# translated with help of chatgpt

from generate_user_file import generate_user_file
from read_cards import generate_cards_db
from read_decks import generate_decks_file
from generate_cards import print_units_with_levels
from generate_cm import print_combo_mastery_table


def parse_credentials():
    creds_path = 'data/.at_creds'
    with open(creds_path) as f:
        lines = f.readlines()

    user_id = next(line for line in lines if "user_id=" in line).strip().split("=")[1]
    password_hash = next(line for line in lines if "password_hash=" in line).strip().split("=")[1]

    return user_id, password_hash


def inventory():
    TEMP_FILE = "temp/user.json"
    user_id, password_hash = parse_credentials()
    # generate_user_file(TEMP_FILE, user_id, password_hash)

    card_catalog, my_cards = generate_cards_db(TEMP_FILE)
    # lindas = "\n".join([str(card) for card in card_catalog if card.type == "7" and card.cardtype == 'character'])
    # print(lindas)

    rarity_name = ["C", "R", "E", "L", "M"]
    my_inventory = {}
    for card in my_cards:
        rarity = rarity_name[int(card_catalog[card.unit_id].rarity) - 1]
        card_name = card_catalog[card.unit_id].name
        entry = f"{rarity}-{card.level}"

        if card_name not in my_inventory:
            my_inventory[card_name] = [entry]
        else:
            my_inventory[card_name].append(entry)
            my_inventory[card_name].sort(reverse=True)

    sorted_dict = dict(sorted(my_inventory.items()))


    # generate_decks_file(user_id, password_hash)
    # print('2')
    #
    # print_units_with_levels(output_file="output/units-with-stars.txt")
    # print_combo_mastery_table(output_file="output/combo_mastery.txt")
    #


if __name__ == '__main__':
    inventory()
