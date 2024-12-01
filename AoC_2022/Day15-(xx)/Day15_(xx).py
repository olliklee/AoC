# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter
from statistics import mean

year, day = "2022", "15"


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
        content = content.split("\n")
        bea = []
        sen = []
        dist = []
        for c in content:
            temp = c[10:c.index(":")]
            temp2 = c[c.index(":") + 23:]
            x1, y1 = [int(x[2:]) for x in temp.split(", ")]
            x2, y2 = [int(x[2:]) for x in temp2.split(", ")]

            sen.append((x1, y1))
            bea.append((x2, y2))
            dist.append(abs(x1 - x2) + abs(y1 - y2))

    return sen, bea, dist


def solve_a():
    sen, bea, dist = prepare_input(f"Day{day}_input.txt")
    row = 2000000
    occup = set()
    for i in range(len(sen)):

        dist_from_row = abs(sen[i][1] - row)
        amount = dist[i] - dist_from_row
        if amount > 0:
            for x in range(sen[i][0] - amount, sen[i][0] + amount + 1):
                occup.add((x, row))

    occup.difference_update(bea)

    return len([i for i in occup if i[1] == row])


def solve_b():
    sen, bea, dist = prepare_input(f"Day{day}_input.txt")
    rauten = []

    # for sender in range(len(sen)):
    for sender in range(len(sen)):
        occup = set()
        # draw diamonds in manhattan distance
        for i in range(-dist[sender], dist[sender] + 1):
            x, y = sen[sender][0], sen[sender][1]
            d = dist[sender]
            x1, y1 = i + x, d - abs(i) + y
            x2, y2 = i + x, abs(i) - d + y
            occup.add((x1, y1))
            occup.add((x2, y2))

        rauten.append(occup)

    # find intersecting points
    points = []
    i = 0
    while i < len(rauten) - 1:
        for j in range(i + 1, len(rauten)):
            x = rauten[i].intersection(rauten[j])
            if len(x) < 3:
                points += x
        i += 1
    points = sorted([list(x) for x in list(set(points))])

    # test for neighbour points and return the missing beacon frequency
    results = []
    for point in points:
        x, y = point
        if [x + 2, y] in points and [x + 1, y - 1] in points and [x + 1, y + 1] in points:
            results.append(f"{(x + 1) * 4000000 +y} Point :{x+1},{y}")

    return results[0] if len(results) > 1 else results


run(day, year)
