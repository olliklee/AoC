# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2021", "05"


class Field:
    def __init__(self, lines):
        self.lines = lines
        self.matrix = [[0 for _ in range(lines)] for _ in range(lines)]

    def __str__(self):
        result = ""
        for i in range(self.lines):
            for j in range(self.lines):
                result += f"{self.matrix[j][i]:3}"
            result += "\n"
        return result

    def mark_point(self, point):
        self.matrix[point.x][point.y] += 1

    def get_crossings(self):
        counter = 0
        for i in range(self.lines):
            for j in range(self.lines):
                if self.matrix[i][j] > 1:
                    counter += 1
        return counter


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x={self.x} y={self.y})"

    def __repr__(self):
        return f"{self.x}/{self.y}"


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return f"({self.point1.x}/{self.point1.y} -> {self.point2.x}/{self.point2.y})"

    def __repr__(self):
        return f"{self.point1.x},{self.point1.y}->{self.point2.x},{self.point2.y}"

    def draw(self, with_diagonal_lines):  # Gibt alle Punkte der Linie zurück
        points = []
        if self.point1.x == self.point2.x:  # Horizontallinie
            step = -1 if self.point1.y > self.point2.y else 1
            for y in range(self.point1.y, self.point2.y + step, step):
                points.append(Point(self.point1.x, y))
        elif self.point1.y == self.point2.y:  # Vertikallinie
            step = -1 if self.point1.x > self.point2.x else 1
            for x in range(self.point1.x, self.point2.x + step, step):
                points.append(Point(x, self.point1.y))
        else:  # Diagonale
            if with_diagonal_lines:
                step_x = -1 if self.point1.x > self.point2.x else 1
                step_y = -1 if self.point1.y > self.point2.y else 1
                x = self.point1.x
                y = self.point1.y
                points.append(Point(x, y))
                while x != self.point2.x:
                    x += step_x
                    y += step_y
                    points.append(Point(x, y))

        return points


def read_input():
    return load_input().split('\n')


def convert_to_point(point_list):
    return Point(int(point_list[0]), int(point_list[1]))


def solve():
    line_koos = []
    matrix_a = Field(1000)
    matrix_b = Field(1000)
    data = read_input()

    # Liest alle Linien ein
    for data_line in data:
        points = data_line.split(" -> ")
        point1 = convert_to_point(points[0].split(","))
        point2 = convert_to_point(points[1].split(","))
        line_koos.append(Line(point1, point2))

   # trage die Linienpunkte in die Matrix ein
    for line in line_koos:
        line_points = line.draw(False)
        for point in line_points:
            matrix_a.mark_point(point)

        line_points = line.draw(True)
        for point in line_points:
            matrix_b.mark_point(point)

    part_a = matrix_a.get_crossings()
    part_b = matrix_b.get_crossings()

    return part_a, part_b


### ----------- Start ------------- ###

run_puzzle(day, year, solve)