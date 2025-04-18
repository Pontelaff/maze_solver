import unittest
import time

from unittest.mock import MagicMock
from maze import Maze
from graphics import Point

class TestMaze(unittest.TestCase):
    def test_create_cells(self):
        cols = 3
        rows = 4
        maze = Maze(Point(10, 15), cols, rows, 10, 10)

        self.assertEqual(len(maze._cells), cols)
        self.assertEqual(len(maze._cells[0]), rows)

    def test_create_cells2(self):
        cols = 3
        rows = 2
        cell_width = 50
        cell_height = 40
        maze = Maze(Point(0, 0), cols, rows, cell_width, cell_height)

        self.assertEqual(len(maze._cells), cols)
        self.assertEqual(len(maze._cells[0]), rows)
        self.assertEqual(maze._cell_height, cell_height)
        self.assertEqual(maze._cell_width, cell_width)

    def test_break_entrance_and_exit(self):
        canvas_mock = MagicMock()
        maze = Maze(Point(0, 0), 3, 2, 10, 10, canvas_mock)
        maze._animation_delay_sec = 0
        maze._break_entrance_and_exit()
        self.assertEqual(maze._cells[0][0].has_left_wall, False)
        self.assertEqual(maze._cells[2][1].has_right_wall, False)
        self.assertEqual(canvas_mock.redraw.call_count, 2)

    def test_init_cells(self):
        rows = 2
        cols = 3
        canvas_mock = MagicMock()
        maze = Maze(Point(0, 0), cols, rows, 10, 10, canvas_mock)
        maze._animation_delay_sec = 0
        maze._init_cells()
        self.assertEqual(canvas_mock.redraw.call_count, rows * cols)

    def test_set_up_runtime(self):
        rows = 12
        cols = 12
        canvas_mock = MagicMock()
        maze = Maze(Point(0, 0), cols, rows, 10, 10, canvas_mock)

        start_time = time.time()
        maze.set_up()
        elapsed_time = time.time() - start_time

        self.assertGreater(elapsed_time, 3)
        self.assertLess(elapsed_time, 5)

    def test_break_walls_recursive(self):
        rows = 5
        cols = 5
        canvas_mock = MagicMock()
        maze = Maze(Point(0,0), rows, cols, 10, 10, canvas_mock)
        maze._animation_delay_sec = 0
        maze._break_walls_recursive(0, 0)

        for i in range(cols):
            for j in range(rows):
                num_walls = int(maze._cells[i][j].has_left_wall)
                num_walls += int(maze._cells[i][j].has_top_wall)
                num_walls += int(maze._cells[i][j].has_right_wall)
                num_walls += int(maze._cells[i][j].has_bottom_wall)
                self.assertLess(num_walls, 4)

    def test_reset_visited(self):
        rows = 5
        cols = 5
        canvas_mock = MagicMock()
        maze = Maze(Point(0,0), rows, cols, 10, 10, canvas_mock)
        maze._animation_delay_sec = 0
        maze._break_walls_recursive(0, 0)
        maze._reset_visited()

        for i in range(cols):
            for j in range(rows):
                self.assertEqual(maze._cells[i][j].visited, False)

if __name__ == "__main__":
    unittest.main()