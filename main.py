from window import *
from tkinter import Tk, BOTH, Canvas


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 10), Point(100, 100)), "red")
    win.draw_line(Line(Point(10, 100), Point(100, 10)), "blue")
    win.draw_line (Line(Point(500, 10), Point(10, 100)), "green")
    win.wait_for_close()

main()