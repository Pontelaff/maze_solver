from tkinter import Tk, BOTH, Canvas


class Point():
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y


class Line():
    def __init__(self, start_point: Point, end_point: Point):
        self.p1 = start_point
        self.p2 = end_point

    def draw(self, canvas: Canvas, color: str) -> None:
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=2)


class Cell():
    def __init__(self, win: "Window", top_left: Point, bottom_right: Point):
        if top_left.x > bottom_right.x or top_left.y > bottom_right.y:
            raise ValueError("Cell expects top-left and bottom-right point as input")
        self.__win = win
        self.__p1 = top_left
        self.__p2 = bottom_right
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def __repr__(self) -> str:
        return f"Cell({self.__p1.x:.0f}, {self.__p1.y:.0f}, {self.has_left_wall}, {self.has_top_wall}, {self.has_right_wall}, {self.has_bottom_wall})"

    def draw(self, color: str) -> None:
        # Draw walls based on top-left and bottom-right points
        if self.has_left_wall:
            self.__win.draw_line(Line(self.__p1, Point(self.__p1.x, self.__p2.y)), color)
        else:
            self.__win.draw_line(Line(self.__p1, Point(self.__p1.x, self.__p2.y)), "white")
        if self.has_top_wall:
            self.__win.draw_line(Line(self.__p1, Point(self.__p2.x, self.__p1.y)), color)
        else:
            self.__win.draw_line(Line(self.__p1, Point(self.__p2.x, self.__p1.y)), "white")
        if self.has_right_wall:
            self.__win.draw_line(Line(self.__p2, Point(self.__p2.x, self.__p1.y)), color)
        else:
            self.__win.draw_line(Line(self.__p2, Point(self.__p2.x, self.__p1.y)), "white")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(self.__p2, Point(self.__p1.x, self.__p2.y)), color)
        else:
            self.__win.draw_line(Line(self.__p2, Point(self.__p1.x, self.__p2.y)), "white")

    def draw_path(self, other: object, undo: bool = False) -> None:
        if not isinstance(other, Cell):
            raise NotImplementedError("Can only draw path to other cell object")

        if undo:
            color = "gray"
        else:
            color = "red"
        start = Point(self.__p1.x + (self.__p2.x - self.__p1.x)/2, self.__p1.y + (self.__p2.y - self.__p1.y)/2)
        end = Point(other.__p1.x + (other.__p2.x - other.__p1.x)/2, other.__p1.y + (other.__p2.y - other.__p1.y)/2)
        self.__win.draw_line(Line(start, end), color)


class Window():
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.wm_title("Maze Solver")
        self.__canvas = Canvas(self.__root, background="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running == True:
            self.redraw()

    def close(self) -> None:
        self.__is_running = False

    def draw_line(self, line: Line, color: str) -> None:
        line.draw(self.__canvas, color)
