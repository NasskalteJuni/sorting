from tkinter import *

white = "#EEE"
font = "Helvetica"
gray = "#222"
orange = "#FFDD00"
cyan = "cyan"
light_gray = "#666"
all_height = 400
all_width = 500

class StyleManager:

    __window = None

    def __init__(self, window):
        self.__window = window

    def init_style(self):
        self.__window.title("SortingAlgorithms at work")
        self.__window.geometry("500x450")
        self.__window.resizable(0, 0)
        self.__window.configure(bg=gray)

