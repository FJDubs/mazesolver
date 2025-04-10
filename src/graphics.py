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
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color='black') -> None:
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell():
    def __init__(self, x1, y1, x2, y2, window, l_wall=True, r_wall=True, t_wall=True, b_wall=True) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.window = window
        self.has_left_wall = l_wall
        self.has_right_wall = r_wall
        self.has_top_wall = t_wall
        self.has_bottom_wall = b_wall

    def draw(self) -> None:
        if self.has_left_wall:
            self.window.draw_line(Line(Point(self.x1,self.y1), Point(self.x1, self.y2)))
        if self.has_right_wall:
            self.window.draw_line(Line(Point(self.x2,self.y1), Point(self.x2, self.y2)))
        if self.has_top_wall:
            self.window.draw_line(Line(Point(self.x1,self.y1), Point(self.x2, self.y1))) 
        if self.has_bottom_wall:
            self.window.draw_line(Line(Point(self.x1,self.y2), Point(self.x2, self.y2)))
    
    def draw_move(self, to_cell, undo=False) -> None:
        color = 'red'
        if undo:
            color = 'grey'
        cell_center = Point(abs(self.x1 + self.x2) // 2, abs(self.y1 + self.y2) // 2)
        to_cell_center = Point(abs(to_cell.x1 + to_cell.x2) // 2, abs(to_cell.y1 + to_cell.y2) // 2)
        self.window.draw_line(Line(cell_center, to_cell_center), color)
