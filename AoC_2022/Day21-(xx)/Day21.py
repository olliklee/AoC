# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter

year, day = "2022", "21"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final


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
        inp_dict = {}
        for line in f.read().split("\n"):
            yell = line[6:].split()
            inp_dict[line[:4]] = tuple(line[6:].split()) if len(yell) > 1 else int(yell[0])

    return inp_dict


def solve_a():
    monkeys = prepare_input(filename)
    expressions = {key: value for key, value in monkeys.items() if type(monkeys[key]) is tuple}
    while len(expressions) > 0:
        for key, value in expressions.items():
            if type(monkeys[value[0]]) is int and type(monkeys[value[2]]) is int:
                monkeys[key] = int(eval(f"{monkeys[value[0]]}{value[1]}{monkeys[value[2]]}"))
                del expressions[key]
                break

    return monkeys["root"]


def solve_b():
    monkeys = prepare_input(filename)
    monkeys["root"] = (monkeys["root"][0], "==", monkeys["root"][2])
    counter = 3360561285172
    results = []
    while True:
        monkey_try = monkeys.copy()
        monkey_try["humn"] = counter
        expressions = {key: value for key, value in monkeys.items() if type(monkeys[key]) is tuple}

        while len(expressions) > 0:
            for key, value in expressions.items():
                if type(monkey_try[value[0]]) is int and type(monkey_try[value[2]]) is int:
                    if key == "root":
                        results.append((counter, monkey_try[value[0]] - monkey_try[value[2]]))
                    monkey_try[key] = int(eval(f"{monkey_try[value[0]]}{value[1]}{monkey_try[value[2]]}"))
                    del expressions[key]
                    break

        if monkey_try["root"]:
            break

        counter += 1

    return counter


run(day, year)
