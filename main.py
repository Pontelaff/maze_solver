#!/usr/bin/env python3
import sys
from graphics import Window, Point
from maze import Maze

def init_maze(win: Window, window_width: int, window_height: int) -> Maze:
    cell_size = 50
    min_border = 25
    maze_width = (window_width - min_border) // cell_size
    maze_height = (window_height - min_border) // cell_size
    x0 = (window_width - maze_width * cell_size) / 2
    y0 = (window_height - maze_height * cell_size) / 2
    maze =  Maze(win, Point(x0, y0), maze_width, maze_height, cell_size, cell_size)
    maze.animate()

    return maze

def main() -> int:
    window_width = 1337
    window_height = 420
    win = Window(window_width, window_height)
    maze = init_maze(win, window_width, window_height)
    win.wait_for_close()

    return 0

if __name__ == "__main__":
    sys.exit(main())
