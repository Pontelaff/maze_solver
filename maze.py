import time
from graphics import Window, Cell, Point

class Maze():
    def __init__(self, top_left: Point, cols: int, rows: int, cell_width: int, cell_height: int, win: Window = None):
        self.__window = win
        self._anchor = top_left
        self._num_cols = cols
        self._num_rows = rows
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._animation_delay_sec = 3 / (self._num_cols * self._num_rows)

        self._create_cells()

    def _create_cells(self) -> None:
        self._cells: list[list[Cell]]= []
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                x0 = self._anchor.x + self._cell_width * i
                y0 = self._anchor.y + self._cell_height * j
                col.append(Cell(self.__window, Point(x0, y0), Point(x0 + self._cell_width, y0 + self._cell_height)))
            self._cells.append(col)

    def _draw_cell(self, i: int, j: int) -> None:
        self._cells[i][j].draw("black")

    def _break_entrance_and_exit(self) -> None:
        # Break entrance (left wall of first cell)
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self.__window.redraw()
        time.sleep(self._animation_delay_sec)

        # Break exit (right wall of last cell)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
        self.__window.redraw()

    def animate(self) -> None:
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
                self.__window.redraw()
                time.sleep(self._animation_delay_sec)

        self._break_entrance_and_exit()


