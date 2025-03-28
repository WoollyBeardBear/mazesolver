from graphics import *
from maze import *
from tkinter import Tk, BOTH, Canvas


def main():
    num_rows = 15
    num_cols = 15
    margin = 50
    screen_x = 800
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()
    win.wait_for_close()
    

main()