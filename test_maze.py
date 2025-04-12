import unittest

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


if __name__ == "__main__":
    unittest.main()