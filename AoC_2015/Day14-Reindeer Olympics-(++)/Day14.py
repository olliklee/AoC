# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

import re

from aoc_helper import *

year, day = "2015", "14"


def get_distance(reindeer, second):
    speed, duration, pause = reindeer
    interval = duration + pause
    full_intervals = second // interval
    rest = second % interval
    distance = full_intervals * speed * duration + min((duration, rest)) * speed
    return distance


def solve():
    part1 = part2 = 0
    puzzle = load_input()
    pattern = r'(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'

    reindeer_dict = {n: (int(s), int(d), int(r)) for n, s, d, r in re.findall(pattern, puzzle, re.MULTILINE)}

    secs = 2503

    for reindeer in reindeer_dict.values():
        dist = get_distance(reindeer, secs)
        part1 = max(part1, dist)

    scores = {r: 0 for r in reindeer_dict.keys()}

    # calculate for every second seperate
    for sec in range(1, secs):
        ranks = {}
        # check each reindeer
        for reindeer in reindeer_dict.keys():
            # make ranking
            ranks[reindeer] = get_distance(reindeer_dict[reindeer], sec)

        sorted_by_dist = sorted(ranks.items(), key=lambda x: x[1], reverse=True)
        ranks = dict(sorted_by_dist)
        prev = 0
        for reindeer, dist in ranks.items():
            if prev == 0 or prev == dist:
                scores[reindeer] += 1
                prev = dist
            else:
                break

        part2 = max(scores.values())

    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
