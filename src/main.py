from graphics import Window, Line, Point
from maze import Maze


def main():
    win = Window(800, 800)
    line_one = Line(Point(10, 50), Point(790,50))
    '''win.draw_line(line_one, 'blue')
    c1 = Cell(20, 60, 60, 100, win, True, True, True, False)
    c1.draw()
    c2 = Cell(20, 100, 60, 140, win, True, True, False, True)
    c2.draw()
    c1.draw_move(c2)'''

    maze = Maze(40, 40, 10, 10, 60, 60, win)
    maze._create_cells()

    win.wait_for_close()


main()