# https://github.com/toddhodes/AnimationThrowdown
# translated with help of chatgpt
from functions.buy_golden_turd import buy_golden_turd_items
from functions.items_inventory import get_items_inventory
from generate_user_file import generate_user_file
from functions.cards_inventory import get_card_inventory
from classes import CardsDB, MyCardsDB
# from read_decks import generate_decks_file
from generate_cards import print_units_with_levels
from generate_cm import print_combo_mastery_table

from consts import CREDITS_PATH, USER_FILE_PATH


def parse_credentials():
    with open(CREDITS_PATH) as f:
        lines = f.readlines()

    user_id = next(line for line in lines if "user_id=" in line).strip().split("=")[1]
    password_hash = next(line for line in lines if "password_hash=" in line).strip().split("=")[1]

    return user_id, password_hash


def inventory():
    user_id, password_hash = parse_credentials()
    if input("Regenerate user file? (y/n): ") == "y":
        generate_user_file(USER_FILE_PATH, user_id, password_hash)

    # Zuerst CardDB laden
    cards_db = CardsDB.from_user_file(USER_FILE_PATH)
    print(f"Cards DB loaded with {len(cards_db.cards)} cards")

    # Dann MyCardsDB mit Referenz zur CardDB laden
    my_cards_db = MyCardsDB.from_user_file(USER_FILE_PATH, cards_db)
    print(f"My Cards loaded with {len(my_cards_db.cards)} cards")

    # Inventar ausgeben
    my_cards_db.print_cards_inventory()
    print(cards_db.cards["40002"])

    if input("\nGenerate item inventory? (y/n): ") == "y":
        get_items_inventory()
        print("Item inventory created under output/item_inventory.txt")



def buy_golden_turd_card(cards_db):
    user_id, password_hash = parse_credentials()

    if input('Buy a new card with golden Turds (y/n)?') == 'y':
        new_turd_buy = buy_golden_turd_items(user_id, password_hash, count=1)
        print(cards_db[new_turd_buy])

if __name__ == '__main__':
    inventory()
