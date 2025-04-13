# https://github.com/toddhodes/AnimationThrowdown
# translated with help of chatgpt

from read_cards import generate_cards_file
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
    user_id, password_hash = parse_credentials()
    
    generate_cards_file(user_id, password_hash)
    generate_decks_file(user_id, password_hash)
    print_units_with_levels(output_file="output/units-with-stars.txt")
    print_combo_mastery_table(output_file="output/combo_mastery.txt")
    
if __name__ == '__main__':
    inventory()