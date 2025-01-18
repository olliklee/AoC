# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
from collections import defaultdict

year, day = "2022", "07"

fs = dict()
sizes = defaultdict(int)


def make_filesystem(program):
    dir_tree = []
    pointer = 0

    while pointer < len(program) - 1:
        command = program[pointer].split()
        if command[0] == "$":
            if command[1] == "ls":
                list_dir(program, "/".join(dir_tree).replace("//", "/"), pointer)
            elif command[1] == "cd":
                if command[2] != "..":
                    dir_tree.append(command[2])
                else:
                    del dir_tree[-1]
                active_dir = dir_tree[-1]
            else:
                print("Bad command")
        pointer += 1


def list_dir(progr, dir, pointer):
    contains = []
    pointer += 1

    # get all directory entries and store it in fs dictionary
    while progr[pointer][0] != "$" and pointer < len(progr):
        command = progr[pointer].split()
        contains.append([command[0], command[1]])
        if pointer < len(progr) - 1:
            pointer += 1
        else:
            break

    if dir in fs:
        fs[dir].append(contains)
    else:
        fs[dir] = contains


def get_size(path, sum=0):
    ls = fs[path]
    for i in range(len(ls)):
        entry = ls[i]
        if entry[0] != "dir":
            sizes[path] += int(entry[0])
        else:
            new_dir = f"{path}/{entry[1]}".replace("//", "/")
            sizes[path] += get_size(new_dir, sizes[path])

    return sizes[path]


def solve():
    program = load_input(split_by_line=True)
    make_filesystem(program)
    get_size("/")

    part1 = sum([value for _, value in sizes.items() if value <= 100000])

    necessary_size = 30000000 - (70000000 - sizes["/"])
    part2 = sorted([size for size in sizes.values() if size > necessary_size])[0]

    return part1, part2


run_puzzle(day, year, solve)
