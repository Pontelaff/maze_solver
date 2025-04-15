import time
import random

from graphics import Window, Cell, Point

class Maze():
    def __init__(self, top_left: Point, cols: int, rows: int, cell_width: int, cell_height: int, win: Window = None, seed: int = None):
        self.__window = win
        self._anchor = top_left
        self._num_cols = cols
        self._num_rows = rows
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._animation_delay_sec = 2 / (self._num_cols * self._num_rows)
        self._seed = random.seed(seed)
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

    def _break_adjacent_walls(self, cell1_x: int, cell1_y: int, cell2_x: int, cell2_y: int) -> None:
        if cell1_x == cell2_x - 1 and cell1_y == cell2_y:
            self._cells[cell1_x][cell1_y].has_right_wall = False
            self._cells[cell2_x][cell2_y].has_left_wall = False
        elif cell1_x == cell2_x + 1 and cell1_y == cell2_y:
            self._cells[cell1_x][cell1_y].has_left_wall = False
            self._cells[cell2_x][cell2_y].has_right_wall = False
        elif cell1_y == cell2_y - 1 and cell1_x == cell2_x:
            self._cells[cell1_x][cell1_y].has_bottom_wall = False
            self._cells[cell2_x][cell2_y].has_top_wall = False
        elif cell1_y == cell2_y + 1 and cell1_x == cell2_x:
            self._cells[cell1_x][cell1_y].has_top_wall = False
            self._cells[cell2_x][cell2_y].has_bottom_wall = False
        else:
            raise ValueError("Cells are not adjacent")

        self._draw_cell(cell1_x, cell1_y)
        self._draw_cell(cell2_x, cell2_y)
        self.__window.redraw()
        time.sleep(self._animation_delay_sec)

    def _break_walls_recursive(self, i: int, j: int) -> None:
        self._cells[i][j].visited = True
        while True:
            new_neighbors = []
            if i > 0 and not self._cells[i - 1][j].visited:
                new_neighbors.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                new_neighbors.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                new_neighbors.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                new_neighbors.append((i, j + 1))
            if not new_neighbors:
                break
            next_i, next_j = random.choice(new_neighbors)
            self._break_adjacent_walls(i, j, next_i, next_j)
            self._break_walls_recursive(next_i, next_j)

    def animate(self) -> None:
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _reset_visited(self) -> None:
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

        self._break_walls_recursive(0, 0)
        self._break_entrance_and_exit()
        self._reset_visited()
