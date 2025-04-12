import unittest

from unittest.mock import MagicMock
from graphics import Point, Cell, Window, Line


class TestPoint(unittest.TestCase):
    def test_point_creation(self):
        p = Point(5, 10)
        self.assertEqual(p.x, 5)
        self.assertEqual(p.y, 10)


class TestLine(unittest.TestCase):
    def test_line_creation(self):
        p1 = Point(0, 0)
        p2 = Point(10, 10)
        line = Line(p1, p2)
        self.assertEqual(line.p1, p1)
        self.assertEqual(line.p2, p2)

    def test_line_draw_calls_canvas(self):
        canvas_mock = MagicMock()
        p1 = Point(0, 0)
        p2 = Point(10, 10)
        line = Line(p1, p2)
        line.draw(canvas_mock, "black")
        canvas_mock.create_line.assert_called_once_with(p1.x, p1.y, p2.x, p2.y, fill="black", width=2)


class TestCell(unittest.TestCase):
    def setUp(self):
        self.mock_window = MagicMock(spec=Window)
        self.top_left = Point(0, 0)
        self.bottom_right = Point(10, 10)
        self.cell = Cell(self.mock_window, self.top_left, self.bottom_right)

    def test_cell_creation_defaults(self):
        self.assertTrue(self.cell.has_left_wall)
        self.assertTrue(self.cell.has_top_wall)
        self.assertTrue(self.cell.has_right_wall)
        self.assertTrue(self.cell.has_bottom_wall)

    def test_cell_invalid_points_raises(self):
        with self.assertRaises(ValueError):
            Cell(self.mock_window, Point(10, 10), Point(5, 5))

    def test_set_walls(self):
        self.cell.set_walls(False, True, False, True)
        self.assertFalse(self.cell.has_left_wall)
        self.assertTrue(self.cell.has_top_wall)
        self.assertFalse(self.cell.has_right_wall)
        self.assertTrue(self.cell.has_bottom_wall)

    def test_draw_calls_draw_line_correctly(self):
        self.cell.set_walls(True, False, False, False)
        self.cell.draw("blue")
        self.mock_window.draw_line.assert_called_once()

    def test_draw_path_valid(self):
        other_cell = Cell(self.mock_window, Point(10, 0), Point(20, 10))
        self.cell.draw_path(other_cell)
        self.mock_window.draw_line.assert_called()

    def test_draw_path_invalid(self):
        with self.assertRaises(NotImplementedError):
            self.cell.draw_path("not_a_cell")


class TestWindow(unittest.TestCase):
    def test_window_creation_and_close_flag(self):
        win = Window(200, 200)
        self.assertFalse(win._Window__isRunnning)
        win.close()
        self.assertFalse(win._Window__isRunnning)

    def test_draw_line_delegates(self):
        win = Window(200, 200)
        line = MagicMock(spec=Line)
        win.draw_line(line, "green")
        line.draw.assert_called()


if __name__ == "__main__":
    unittest.main()