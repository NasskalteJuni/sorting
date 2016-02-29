from tkinter import *
from view.StyleManager import *


class MainWindow:

    __main_window = None
    __main_controller = None



    def __init__(self, window, main_controller):
        self.__main_controller = main_controller
        self.__main_window = window

    def show_menu(self, algorithm_dict):
        menu = Menu(self.__main_window)
        self.__main_window.config(menu=menu)
        dropdown_algorithm_menu = Menu(menu, tearoff=0)
        for algorithm in algorithm_dict:
            dropdown_algorithm_menu.add_command(label=algorithm, command=self.__main_controller.set_algorithm(algorithm_dict[algorithm]))
        menu.add_cascade(label="algorithms", menu=dropdown_algorithm_menu)
        menu.add_command(label="edit list", command=self.__main_controller.show_lists)
