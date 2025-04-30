from classes import UserItems
from consts import USER_FILE_PATH


def get_items_inventory(write_file=True):
    items = UserItems.from_user_file(USER_FILE_PATH)
    if write_file:
        items.write_items_inventory()

    return items
