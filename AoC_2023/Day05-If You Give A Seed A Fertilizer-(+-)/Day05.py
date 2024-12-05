# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from re import findall

year, day = "2023", "05"

def prepare_input():
    content = load_input(test= True, delimiter="\n\n")

    seeds = list(map(int, findall("\d+", content[0])))
    maps = {block: list(map(int, findall("\d+", content[block]))) for block in range(1, len(content))}
    maps_ranges = {}
    for single_map in maps.keys():
        maps_ranges[single_map] = []
        transform = maps[single_map]
        for j in range(0, len(transform), 3):
            maps_ranges[single_map].append((transform[j+1], transform[j], transform[j+2]))

    return seeds, maps_ranges


def translate_spot(seed, translation):
    return seed + translation[1] - translation[0] if translation[0] <= seed < translation[0] + translation[2] else seed


def solve_a():
    seed_spots = []
    for seed in my_seeds:
        spot = seed
        for category in my_maps.values():
            for my_range in category:
                spot = translate_spot(spot, my_range)

        seed_spots.append(spot)
    return min(seed_spots) # 382895070


def solve_b():
    # new seeds
    new_seeds = []

    for i in range(0, len(my_seeds), 2):
        start, amount = my_seeds[i], my_seeds[i + 1]
        new_seeds.append(range(start, start + amount))
    #print(new_seeds)
    # seed_spots = []
    # for seed in new_seeds:
    #     spot = seed
    #     for category in my_maps.values():
    #         for translation in category:
    #             new_spot = translate_spot(spot, translation)
    #             if new_spot != spot:
    #                 spot = new_spot
    #
    #                 break
    #
    #     seed_spots.append(spot)
    #
    # return min(seed_spots)
    return 0

### ----------- Start ------------- ###

my_seeds, my_maps = prepare_input()
run_puzzles(day, year, solve_a, solve_b)
