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
    def test_cell_creation_defaults(self):
        mock_window = MagicMock(spec=Window)
        top_left = Point(0, 0)
        bottom_right = Point(10, 10)
        cell = Cell(mock_window, top_left, bottom_right)

        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_bottom_wall)

    def test_cell_invalid_points_raises(self):
        mock_window = MagicMock(spec=Window)
        with self.assertRaises(ValueError):
            Cell(mock_window, Point(10, 10), Point(5, 5))

    def test_draw_calls_draw_line_correctly(self):
        mock_window = MagicMock(spec=Window)
        top_left = Point(0, 0)
        bottom_right = Point(10, 10)
        cell = Cell(mock_window, top_left, bottom_right)

        cell.has_left_wall = False
        cell.draw("blue")
        self.assertEqual(mock_window.draw_line.call_count, 4)

    def test_draw_path_valid(self):
        mock_window = MagicMock(spec=Window)
        cell1 = Cell(mock_window, Point(0, 0), Point(10, 10))
        cell2 = Cell(mock_window, Point(10, 0), Point(20, 10))

        cell1.draw_path(cell2)
        mock_window.draw_line.assert_called()

    def test_draw_path_invalid(self):
        mock_window = MagicMock(spec=Window)
        cell = Cell(mock_window, Point(0, 0), Point(10, 10))

        with self.assertRaises(NotImplementedError):
            cell.draw_path("not_a_cell")


class TestWindow(unittest.TestCase):
    def test_window_creation_and_close_flag(self):
        win = Window(200, 200)
        self.assertFalse(win._Window__is_running)
        win.close()
        self.assertFalse(win._Window__is_running)

    def test_draw_line_delegates(self):
        win = Window(200, 200)
        line = MagicMock(spec=Line)
        win.draw_line(line, "green")
        line.draw.assert_called()


if __name__ == "__main__":
    unittest.main()