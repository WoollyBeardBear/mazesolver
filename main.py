from graphics import *
from tkinter import Tk, BOTH, Canvas


def main():
    win = Window(800, 600)
    c1 = Cell(win)
    c1.draw(0, 0, 100, 100)
    c2 = Cell(win)
    c2.draw(100, 0, 200, 100)
    c1.draw_move(c2)
    win.wait_for_close()

main()