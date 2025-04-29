import json

from consts import USER_FILE_PATH, JS_SIEGE


def get_siege_setup():
    with open(USER_FILE_PATH) as f:
        data = json.load(f)[JS_SIEGE]

    enemy_name = data.get('enemy_faction_name', 'Unknown')
    enemy_rank = data.get('enemy_rank', 'Unknown')

    enemy_users = _get_users(data, 'enemy_locations')
    our_users = _get_users(data, 'locations')
    our_rank = data.get('rank', 'Unknown')

    _print_user_list(f"Us #{our_rank}", our_users)
    _print_user_list(f'{enemy_name} #{enemy_rank}', enemy_users)


def _get_users(data, which):
    all_users = {}
    for location_id, location_data in data.get(which, {}).items():
        # Unterschied beachten: bei enemy_locations verschachtelt ("data"), bei available_locations direkt
        if ('data') in location_data:
            island_name = location_data['data']['name']
            user_list = location_data.get('users', [])
        else:
            island_name = location_data['name']
            user_list = location_data.get('users', [])

        user_map = {user['user_id']: user['name'] for user in user_list}
        all_users[island_name] = user_map
    return all_users


def _print_user_list(title, user_list, simple=True):
    print(f'\n{title}\n{"-" * len(title)}')
    for island_name, user_map in user_list.items():
        user_output = ", ".join(user_map.values()) \
            if simple else ", ".join(f"{name} ({user_id})" for user_id, name in user_map.items())

        print(f'  {island_name:25} {user_output}')

get_siege_setup()