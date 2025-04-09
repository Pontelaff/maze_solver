from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.wm_title("Maze Solver")
        self.__canvas = Canvas(self.__root, background="white", height=self.__height, width=self.__width)
        self.__canvas.pack()
        self.__isRunnning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__isRunnning = True
        while self.__isRunnning == True:
            self.redraw()

    def close(self) -> None:
        self.__isRunnning = False
