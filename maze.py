from graphics import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    # NOTE: self._cells[i][j] -> i = COLUMN, j = ROW (column-major order)
    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cells(i,j)
    
    def _draw_cells(self, i, j):
        if self.win is None:
            return
        cell = self._cells[i][j]
        cellx1 = self.x1 + (i * self.cell_size_x)
        cellx2 = self.x1 + (i * self.cell_size_x) + self.cell_size_x
        celly1 = self.y1 + (j * self.cell_size_y)
        celly2 = self.y1 + (j * self.cell_size_y) + self.cell_size_y
        cell.draw(cellx1, celly1, cellx2, celly2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self.num_cols - 1][self.num_rows - 1]
        entrance.has_top_wall = False
        exit.has_bottom_wall = False
        self._draw_cells(0, 0)
        self._draw_cells(self.num_cols -1, self.num_rows -1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < self.num_cols and 0 <= nj < self.num_rows:
                    if not self._cells[ni][nj].visited:
                        to_visit.append((ni, nj))
            if not to_visit:
                self._draw_cells(i, j)
                return
            rand_direction = random.randrange(0, len(to_visit))
            ni, nj = to_visit[rand_direction]

            di, dj = ni - i, nj - j

            if di == 1 and dj == 0:
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
            elif di == -1 and dj == 0:
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
            elif di == 0 and dj == 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
            elif di == 0 and dj == -1:
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
                
            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col: 
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        print(f"cell {i} {j}")
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for di, dj in directions:
            print(f"testing {di}, {dj}")
            if di == 1 and not self._cells[i][j].has_right_wall:
                ni = i + di
                if ni < self.num_cols and not self._cells[ni][j].visited:
                    print(f"drawing move {ni}, {j}")
                    self._cells[i][j].draw_move(self._cells[ni][j])
                    result = self._solve_r(ni, j)
                    if result == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[ni][j], True)
            elif di == -1 and not self._cells[i][j].has_left_wall:
                ni = i + di
                if ni >= 0 and not self._cells[ni][j].visited:
                    print(f"drawing move {ni}, {j}")
                    self._cells[i][j].draw_move(self._cells[ni][j])
                    result = self._solve_r(ni, j)
                    if result == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[ni][j], True)
            elif dj == 1 and not self._cells[i][j].has_bottom_wall:
                nj = j + dj
                if nj < self.num_rows and not self._cells[i][nj].visited:
                    print(f"drawing move {i}, {nj}")
                    self._cells[i][j].draw_move(self._cells[i][nj])
                    result = self._solve_r(i, nj)
                    if result == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i][nj], True)
            elif dj == -1 and not self._cells[i][j].has_top_wall:
                nj = j + dj
                if nj >= 0 and not self._cells[i][nj].visited:
                    print(f"drawing move {i}, {nj}")
                    self._cells[i][j].draw_move(self._cells[i][nj])
                    result = self._solve_r(i, nj)
                    if result == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i][nj], True)
            print(f"not {di} {dj}")
        print("False")
        return False

            
        

        

    