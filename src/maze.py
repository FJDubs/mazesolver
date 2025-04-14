from cell import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        if self.seed is not None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = []
        for i in range(self.num_cols):
            cell_col = []
            for j in range(self.num_rows):
                cell = Cell(self.x1 + (i * self.cell_size_x),
                            self.y1 + (j * self.cell_size_y),
                            self.x1 + self.cell_size_x + (i * self.cell_size_x),
                            self.y1 + self.cell_size_y + (j * self.cell_size_y),
                            self.win)
                cell_col.append(cell)
            self._cells.append(cell_col)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                if self.win is not None:
                    self._draw_cells(i, j)
        self._break_entrance_and_exit()

    def _draw_cells(self, i , j) -> None:
        if self.win is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self) -> None:
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self) -> None:
        entrance = self._cells[0][0]
        exit = self._cells[self.num_cols - 1][self.num_rows - 1]
        exit.has_bottom_wall = False
        entrance.has_top_wall = False
        if self.win is not None:
            entrance.draw()
            exit.draw()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        
    def _break_walls_r(self, i, j) -> None:
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append(('left', i - 1, j))
            if i <  self.num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append(('right', i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append(('up', i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append(('down', i, j + 1))
            if to_visit == []:
                if self.win is not None:
                    current_cell.draw()
                return
            next_cell = random.choice(to_visit)
            match next_cell[0]:
                case 'up':
                    current_cell.has_top_wall = False
                    self._cells[next_cell[1]][next_cell[2]].has_bottom_wall = False
                case 'down':
                    current_cell.has_bottom_wall = False
                    self._cells[next_cell[1]][next_cell[2]].has_top_wall = False
                case 'left':
                    current_cell.has_left_wall = False
                    self._cells[next_cell[1]][next_cell[2]].has_right_wall = False
                case 'right':
                    current_cell.has_right_wall = False
                    self._cells[next_cell[1]][next_cell[2]].has_left_wall = False
            self._break_walls_r(next_cell[1], next_cell[2])
            if self.win is not None:
                self._animate()

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False