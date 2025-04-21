from graphics import Window, Line, Point
from maze import Maze


def main():
    win = Window(800, 800)
    maze = Maze(40, 40, 10, 10, 60, 60, win, 0)
    maze.solve()
    print('done')

    win.wait_for_close()


main()