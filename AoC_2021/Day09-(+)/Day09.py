deepest = []


def read_input_from_file(file_name):
    data = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            line = list(line)
            data.append(line)
    return data


def is_lowest_point(x, y, data):
    value = value_at(x, y, data)
    neighbour_up = 9 if y < 2 else int(data[y - 2][x - 1])
    neighbour_down = 9 if y > len(data) - 1 else int(data[y][x - 1])
    neighbour_left = 9 if x < 2 else int(data[y - 1][x - 2])
    neighbour_right = 9 if x > len(data[0]) - 1 else int(data[y - 1][x])
    lowest_neighbours = min([neighbour_up, neighbour_down, neighbour_right, neighbour_left])
    return value < lowest_neighbours


def value_at(x, y, data):
    return int(data[y - 1][x - 1])


def get_deepest_points(data):
    deepest_points = []
    for i in range(1, len(data[0]) + 1):
        for j in range(1, len(data) + 1):
            if is_lowest_point(i, j, data):
                deepest_points.append([j, i])
    return deepest_points


def solve_09a():
    riddle = read_input_from_file("input.txt")

    risklevel = 0
    for i in range(1, len(riddle[0]) + 1):
        for j in range(1, len(riddle) + 1):
            if is_lowest_point(i, j, riddle):
                risklevel += value_at(i, j, riddle) + 1

    return risklevel


# def solve_09b():
#     riddle = read_input_from_file("input_test.txt")
#
#     basin_points = []
#     deepest_points = get_deepest_points(riddle)
#     for point in deepest_points:
#         basin_points = get_basin_size(point, data)



print(f"Day 09 - Part 1: {solve_09a()}")
# print(f"Day 09 - Part 2: {solve_09b()}")
