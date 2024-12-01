# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter

year, day = "2022", "09"


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
        way = content.split("\n")

    return way


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return f"({self.x},{self.y})"

    def move(self, direction):
        m = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
        self.x += m[direction][0]
        self.y += m[direction][1]


class LongRope:
    def __init__(self, points: [Point]):
        self.points = points
        self.lastmoved = False

    def __str__(self):
        output = ""
        for p in self.points:
            output += f"({p.x},{p.y})->"
        return output.strip("->")

    def __repr__(self):
        output = ""
        for p in self.points:
            output += f"({p.x},{p.y})->"
        return output.strip("->")

    def move(self, num, direction):
        if num >= len(self.points):
            return "Done"

        head = self.points[num]
        tail = self.points[num + 1]
        head.move(direction)

        if direction in ['U', 'D']:
            if abs(tail.y - head.y) > 1:
                tail.x = head.x
                if abs(tail.y - head.y) > 1:
                    tail.move(direction)
                    self.lastmoved = True
        else:
            if abs(tail.x - head.x) > 1:
                tail.y = head.y
                if abs(tail.x - head.x) > 1:
                    tail.move(direction)
                    self.lastmoved = True

        self.points[num], self.points[num + 1] = head, tail

    def fullmove(self, direction):
        for i in range(len(self.points)-1):
            self.move(i, direction)
            if not self.lastmoved:
                break
        self.lastmoved = True

    def printgraphic(self):
        print(self.points)
        for y in range(-5,5):
            for x in range(-5,5):
                if Point(x,y) in self.points:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
    # def move(self, direction, times=1):
    #     for i in range(times):
    #         self.move(direction)
    #         self.follow_tail(direction)
    #         tail_points_a.add((self.tail.x, self.tail.y))



class Rope:
    def __init__(self, head: Point, tail: Point):
        self.head = head
        self.tail = tail

    def __str__(self):
        return f"H{self.head}->{self.tail}"

    def __repr__(self):
        return f"H{self.head}->{self.tail}"

    def move_head(self, direction, times=1):
        for i in range(times):
            self.head.move(direction)
            self.follow_tail(direction)
            tail_points_a.add((self.tail.x, self.tail.y))

    def follow_tail(self, direction):
        if direction in ['U', 'D']:
            if abs(self.tail.y - self.head.y) > 2:
                self.tail.x = self.head.x
            elif (abs(self.tail.y - self.head.y)) > 1:
                    self.tail.move(direction)
        else:
            if abs(self.tail.x - self.head.x) > 2:
                self.tail.y = self.head.y
            elif (abs(self.tail.x - self.head.x)) >1:
                    self.tail.move(direction)


tail_points_a = set()
tail_points_b = set()


def solve_a():
    way = prepare_input(f"Day{day}_input.txt")
    head, tail = Point(0, 0), Point(0, 0)
    rope = Rope(head, tail)

    for m in way:
        d, t = m.split()
        rope.move_head(d, int(t))

    return len(tail_points_a)


def solve_b():
    way = prepare_input(f"Day{day}_input_.txt")
    rope: [Rope] = []
    for i in range(6):
        rope.append(Rope(Point(0,0),Point(0,0)))

    for m in ["R", "R","R","R"]:
        t = 1
        for times in range(int(t)):
            for i in range(len(rope)-1):
                rope[i].move_head(m)
                rope[i+1].head = rope[i].tail

        for i in range(6):
            print(rope[i])




    return len(tail_points_b)


run(day, year)
