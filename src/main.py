from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    line_one = Line(Point(10, 50), Point(790,50))
    win.draw_line(line_one, 'blue')
    c1 = Cell(20, 60, 60, 100, win, True, True, True, False)
    c1.draw()
    c2 = Cell(20, 100, 60, 140, win, True, True, False, True)
    c2.draw()
    c1.draw_move(c2, True)

    win.wait_for_close()


main()