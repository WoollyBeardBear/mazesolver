from graphics import *
from tkinter import Tk, BOTH, Canvas


def main():
    num_cols = 12
    num_rows = 12
    win = Window(800, 600)
    m1 = Maze(200, 200, num_rows, num_cols, 20, 20, win)
    
    win.wait_for_close()
    

main()