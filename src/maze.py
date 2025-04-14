from cell import Cell
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
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
        