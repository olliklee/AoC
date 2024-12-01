# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter
import math

year, day = "2022", "11"


def run(d, y):
    print(f"\nResults from AoC {y} - Day {d}\n{'-' * 30}")

    start = perf_counter()
#    print(f"Day {d} - Part 1: {solve_a()}")

    lap = perf_counter()
    print(f"Day {d} - Part 2: {solve_b()}")

    stop = perf_counter()

    print(f"\nPerformance\n{'-' * 30}")
    print(f"Part 1: {(lap - start) * 100:.6f} ms\nPart 2: {(stop - lap) * 100:.6f} ms")
    print(f"{'-' * 30}\nGesamt: {(stop - start) * 100:.6f} ms")


def prepare_input(file_name):
    monkeydict = {}
    with open(file_name) as f:
        content = f.read()

        content = content.split("\n\n")

        for item in content:
            item = item.split("\n")
            m_id = int(item[0][7:].strip(":"))
            itemlist = list(map(int, item[1][18:].split(", ")))
            op, val = item[2][22:].split()
            cond = int(item[3][21:])
            throw1 = int(item[4][29])
            throw2 = int(item[5][30])

            monkeydict[m_id] = Monkey(itemlist, op, val, cond, throw1, throw2)
        print(monkeydict)
    return monkeydict


class Monkey:
    def __init__(self, itemlist, op, value, cond, throw1, throw2, inspected = 0):
        self.itemlist = itemlist
        self.op = op
        self.value = value
        self.cond = cond
        self.throw1 = throw1
        self.throw2 = throw2
        self.inspected = inspected

    def __str__(self):
        return f"{self.itemlist}"

    def __repr__(self):
        return f"{self.itemlist}"



def monkey_plays_a(id):
    monkey = monkeys_a[id]
    while len(monkey.itemlist) > 0:
        item = monkey.itemlist[0]
        if monkey.op[0] == "*":
            if monkey.op[1] == "old":
                worrylevel = item * item
            else:
                worrylevel = item * int(monkey.op[1])
        else:
            if monkey.op[1] == "old":
                worrylevel = item + item
            else:
                worrylevel = item + int(monkey.op[1])
        worrylevel //= 3

        if worrylevel % monkey.cond == 0:
            target = monkey.throw1
        else:
            target = monkey.throw2
        monkey.inspected += 1
        monkey.itemlist.pop(0)
        throw_to_a(target, worrylevel)

def throw_to_a(id, worrylevel):
    monkeys_a[id].itemlist.append(worrylevel)


def monkey_plays_b(id):
    monkey = monkeys_b[id]
    print(monkey)
    while len(monkey.itemlist) > 0:
        item = monkey.itemlist[0]
        value = int(item if monkey.value == "old" else monkey.value)
        worrylevel = item + value if monkey.op == "+" else item * value
        worrylevel = worrylevel // magic_divisor

        if worrylevel % monkey.cond == 0:
            target = monkey.throw1
        else:
            target = monkey.throw2
        monkey.inspected += 1
        monkey.itemlist.pop(0)
        throw_to_b(target, worrylevel)


def throw_to_b(id, worrylevel):
    monkeys_b[id].itemlist.append(worrylevel)




def solve_a():
    for i in range(20):
        for id in range(len(monkeys_a)):
            monkey_plays_a(id)

    inspectionlist = sorted([monkeys_a[id].inspected for id in monkeys_a.keys()], reverse=True)

    return inspectionlist[0] * inspectionlist[1]


def solve_b():

    for i in range(1):
        for id in range(len(monkeys_b)):
            monkey_plays_b(id)
    insplist = [monkeys_b[id].inspected for id in monkeys_b.keys()]
    print(insplist)
    inspections = math.prod(insplist)
    return inspections

monkeys_a = prepare_input(f"Day{day}_input.txt")
monkeys_b = prepare_input(f"Day{day}_input_.txt")
magic_divisor = math.prod([i.cond for i in monkeys_b.values()])
print(magic_divisor)

run(day, year)
