import unittest
from maze import Maze

class Tests(unittest.TestCase):
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10,seed=0)

    def test_maze_create_cells(self):
        self.assertEqual(
            len(self.m1._cells),
            self.num_cols,
        )
        self.assertEqual(
            len(self.m1._cells[0]),
            self.num_rows,
        )
    def test_maze_break_entrace_and_exit(self):
        self.m1._break_entrance_and_exit()
        self.assertFalse(self.m1._cells[0][0].has_top_wall)
        self.assertFalse(self.m1._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall)
    
    def test_reset_cells_visited(self):
        self.m1._reset_cells_visited()
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.assertFalse(self.m1._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()