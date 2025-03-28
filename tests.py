import unittest
from graphics import *
from maze import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_entrance_exit(self):
        num_cols = 12
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].has_top_wall, False, )
        self.assertFalse(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)

    def test_visited_reset(self):
        num_cols = 12
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].visited, False, )
        self.assertFalse(m1._cells[7][7].visited, False)

if __name__ == "__main__":
    unittest.main()