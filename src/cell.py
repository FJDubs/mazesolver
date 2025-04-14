from graphics import Window, Point, Line

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
        else:
            self.window.draw_line(Line(Point(self.x1,self.y1), Point(self.x1, self.y2)), 'white')

        if self.has_right_wall:
            self.window.draw_line(Line(Point(self.x2,self.y1), Point(self.x2, self.y2)))
        else:
            self.window.draw_line(Line(Point(self.x2,self.y1), Point(self.x2, self.y2)), 'white')

        if self.has_top_wall:
            self.window.draw_line(Line(Point(self.x1,self.y1), Point(self.x2, self.y1)))
        else:
            self.window.draw_line(Line(Point(self.x1,self.y1), Point(self.x2, self.y1)), 'white')
            
        if self.has_bottom_wall:
            self.window.draw_line(Line(Point(self.x1,self.y2), Point(self.x2, self.y2)))
        else:
            self.window.draw_line(Line(Point(self.x1,self.y2), Point(self.x2, self.y2)), 'white')
    
    def draw_move(self, to_cell, undo=False) -> None:
        color = 'red'
        if undo:
            color = 'grey'
        cell_center = Point(abs(self.x1 + self.x2) // 2, abs(self.y1 + self.y2) // 2)
        to_cell_center = Point(abs(to_cell.x1 + to_cell.x2) // 2, abs(to_cell.y1 + to_cell.y2) // 2)
        self.window.draw_line(Line(cell_center, to_cell_center), color)
