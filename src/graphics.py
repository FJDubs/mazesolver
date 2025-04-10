from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
        print('Window Closed...')

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line, fill_color='black') -> None:
        line.draw(self.__canvas, fill_color)


class Point():
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_one, point_two) -> None:
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas, fill_color) -> None:
        canvas.create_line(self.point_one.x, self.point_one.y, self.point_two.x, self.point_two.y, fill=fill_color, width=2)
