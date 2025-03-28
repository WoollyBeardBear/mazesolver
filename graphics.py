import time
import random
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x, self.point1.y, 
            self.point2.x, self.point2.y, 
            fill=fill_color, width=2
        )

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        else:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")      
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")
        else:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")

    
    def draw_move(self, to_cell, undo=False):
        center = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        to_cell_center = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        self._win.draw_line(Line(center, to_cell_center), "red" if not undo else "grey")
