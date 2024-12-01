#  Solutions of Advent of Code
#  Oliver Kleemann

from time import perf_counter

year, day = "2022", "05"

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
    with open(file_name, encoding='utf8') as f:

        cols = [[], [], [], [], [], [], [], [], []]
        orders = []
        for i, line in enumerate(f):
            # parse crate order per stack
            if i < 8:
                for j in range(9):
                    if line[(j * 4) + 1] != " ":
                        cols[j].append(line[(j * 4) + 1])
            # extract order in plain text
            if i > 9:
                orders.append(line)

        # parse orders from plain text into ints
        for i, order in enumerate(orders):
            order_splitted = order.split()
            orders[i] = tuple(map(int, order_splitted[1::2]))

    return cols, orders


def move(cols, order, crane_type):
    # split order into values
    amount = order[0]
    from_col = order[1]
    to_col = order[2]
    
    # lifts crates from stack
    crates_taken = cols[from_col - 1][:amount]
    cols[from_col - 1] = cols[from_col - 1][amount:]

    if crane_type == "9000":
        crates_taken = crates_taken[::-1]
    elif crane_type != "9001":
        raise Exception("Unknown Crane!")

    # puts crates on target stack
    cols[to_col - 1] = crates_taken + cols[to_col - 1]



def solve_a():
    cols, orders = prepare_input(f"Day{day}_input.txt")
    for order in orders:
        move(cols, order, crane_type="9000")

    result = ""
    for col in cols:
        result += col[0]

    return result


def solve_b():
    cols, orders = prepare_input(f"Day{day}_input.txt")
    for order in orders:
        move(cols, order, crane_type="9001")

    result = ""
    for col in cols:
        result += col[0]

    return result


run(day, year)