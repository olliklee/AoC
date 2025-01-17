# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from AoC_2023.aoc_helpers import run_puzzles

year, day = "2023", "10"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final  # change to final when ready

pipes = {
    "|": ("\u2503", (0, 180)),
    "-": ("\u2501", (90, 270)),
    "L": ("\u2517", (0, 90)),
    "J": ("\u251B", (0, 270)),
    "7": ("\u2513", (180, 270)),
    "F": ("\u250F", (180, 90)),
    ".": (" ", ()),
    "S": ("S", (0, 90, 180, 270))
}


def prepare_input():
    with open(filename) as f:
        content = f.read().split("\n")
    return content


def get_next(point, angle) -> tuple:
    x, y = point
    connectors = maze[y][x]

    if angle in connectors:
        if angle == 0:
            return x, y - 1
        elif angle == 90:
            return x + 1, y
        elif angle == 180:
            return x, y + 1
        elif angle == 270:
            return x - 1, y
    else:
        print('Something went wrong')
        return (),


def solve_a():
    counter = 1
    angle = 90
    x, y = get_next(start, angle)
    while True :
        if len(maze[y][x]) == 4:
            break
        counter += 1
        # wohin führt das rohr?
        angle = [element for element in maze[y][x] if element != (angle + 180) % 360][0]
        x, y = get_next((x, y), angle)

    return counter // 2    # am weitesten entfernter Punkt = halbe Gesamtstrecke


def solve_b():

    # code goes here
    return 0


#  ----------   Start   ----------   #

puzzle = prepare_input()
maze = [[pipes[sign][1] for sign in line] for line in puzzle]
maze_optical = "\n".join(["".join([pipes[sign][0] for sign in line]) for line in puzzle])
start = [(x, y) for y, line in enumerate(puzzle) if (x := line.find("S")) > 0][0]

run_puzzles(day, year, solve_a, solve_b)
