from tkinter import *
from view.StyleGuide import *


class MainWindow:

    __main_window = None
    __main_controller = None



    def __init__(self, window, main_controller):
        self.__main_controller = main_controller
        self.__main_window = window
        self.__main_window.title("SortingAlgorithms at work")
        self.__main_window.geometry("500x450")
        self.__main_window.resizable(0, 0)
        self.__main_window.configure(bg="#222")


    def show_menu(self, algorithm_dict):
        menu = Menu(self.__main_window)
        self.__main_window.config(menu=menu)
        dropdown_algorithm_menu = Menu(menu, tearoff=0)
        for algorithm in algorithm_dict:
            def __set_algorithm(given_algorithm):
                def __chose_algorithm():
                    self.__main_controller.set_algorithm(algorithm_dict[given_algorithm])
                return __chose_algorithm
            dropdown_algorithm_menu.add_command(label=algorithm, command=__set_algorithm(algorithm))
        menu.add_cascade(label="algorithms", menu=dropdown_algorithm_menu)
        menu.add_command(label="edit list", command=self.__main_controller.show_lists)
