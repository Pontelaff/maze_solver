#!/usr/bin/env python3
import sys
from graphics import Window, Point, Line, Cell


def main() -> int:
    win = Window(800, 600)
    line = Line(Point(69, 32), Point(420, 123))
    cell1 = Cell(win, Point(10, 10), Point(20, 20))
    cell1.draw("gray")
    cell1.set_walls(False, False, False, True)
    cell1.draw("red")
    cell2 = Cell(win, Point(50, 50), Point(100, 150))
    cell2.set_walls(True, False, True, False)
    cell2.draw("blue")
    win.draw_line(line, "red")
    win.wait_for_close()

    return 0

if __name__ == "__main__":
    sys.exit(main())
