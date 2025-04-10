from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    line_one = Line(Point(10, 50), Point(790,50))
    win.draw_line(line_one, 'blue')
    win.wait_for_close()


main()