# # #  Solutions of Advent of Code
# # #  Oliver Kleemann (mit Hilfe von Gravitar Youtube)

from time import perf_counter

year, day = "2022", "10"


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
        content = content.split('\n')
        content = [line.split() for line in content]
    return content


def solve_a():
    program = prepare_input(f"Day{day}_input.txt")
    register, cycles = [1], [20, 60, 100, 140, 180, 220]
    result = 0
    for com in program:
        register.append(0)
        if com[0] != "noop":
            register.append(int(com[1]))

    for steps in cycles:
        result += sum(register[:steps]) * steps

    return result


def solve_b():
    program = prepare_input(f"Day{day}_input.txt")
    register = 1
    reg = [1]

    for com in program:
        reg.append(register)
        if com[0] != "noop":
            reg.append(register)
            register += int(com[1])

    dsp = ""

    for step in range(0,241):
        dsp += "\n" if not step % 40 else ""
        sprite = reg[step]+1
        if (step % 40 - sprite) in [-1,0,1]:
            dsp += "🟥"
        else:
            dsp += " "

    print (dsp)


run(day, year)
