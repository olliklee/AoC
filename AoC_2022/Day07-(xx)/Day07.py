# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter
from collections import defaultdict

year, day = "2022", "07"


def run(d, y):
    print(f"\nResults from AoC {y} - Day {d}\n{'-' * 30}")

    start = perf_counter()
    print(f"Day {d} - Part 1: {solve_a()}")

    lap = perf_counter()
    print(f"Day {d} - Part 2: {solve_b()}")

    stop = perf_counter()

    print(f"\nPerformance\n{'-' * 30}")
    print(f"Part 1: {(lap - start) * 100:.6f} ms\nPart 2: {(stop - lap) * 100:.6f} ms")
    print(f"{'-' * 30}\nGesamt: {(stop - start) * 100:.6f} ms")


def prepare_input(file_name):
    with open(file_name) as f:
        content = f.read()
        program = content.split("\n")
    return program


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

# The solution
#

fs = dict()
sizes = defaultdict(int)


def solve_a():
    program = prepare_input(f"Day{day}_input.txt")
    make_filesystem(program)
    get_size("/")

    # sum up every directory with a size > 100.000
    sumup = 0
    for _, value in sizes.items():
        if value <= 100000:
            sumup += value

    return sumup


def solve_b():
    necessary_size = 30000000 - (70000000 - sizes["/"])

    suitable_sizes = []
    for size in sizes.values():
        if size > necessary_size:
            suitable_sizes.append(size)

    suitable_sizes.sort()
    return suitable_sizes[0]


run(day, year)
