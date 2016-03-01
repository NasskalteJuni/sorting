from view.MainGui import MainWindow
from controller.ListEditController import ListController
from controller.SortingController import SortingController
from tkinter import Tk
from sorting.bubblesort import bubblesort
from sorting.pancakesort import pancakesort
from sorting.cocktailsort import cocktailsort
from copy import deepcopy
from threading import Thread

class MainController:

    __algorithm_dictionary = None
    __algorithm = None
    __list = None
    __window = None
    __gui = None
    __thread = None
    __list_control = None
    __sort_control = None
    __thread = None

    def __init__(self):
        self.__window = Tk()
        self.__window.title("SortingAlgorithms at work")
        self.__window.geometry("500x450")
        self.__window.resizable(0, 0)
        self.__window.configure(bg="#222")
        self.__gui = MainWindow(self.__window, self)
        self.__algorithm_dictionary = {"bubble sort": bubblesort, "pancake sort": pancakesort, "cocktail sort": cocktailsort}
        self.__algorithm = self.__algorithm_dictionary[self.__get_a_key(self.__algorithm_dictionary)]
        self.__list = [3, 1, 9, 8, 6, 4, 5, 2, 7]

    def start(self):
        self.__gui.show_menu(self.__algorithm_dictionary)
        self.__window.mainloop()

    def set_algorithm(self, algorithm):
        if algorithm is not None:
            if self.__sort_control is not None:
                self.__sort_control.end()
            self.__algorithm = algorithm
            self.__thread = Thread(target=self.show_animation,)
            self.__thread.start()

    def get_algorithm(self):
        return self.__algorithm

    def set_list(self, input_list):
        if input_list is not None and len(input_list) > 0:
            if self.__sort_control is not None:
                self.__sort_control.end()
            self.__list = input_list
            self.__thread = Thread(target=self.show_animation,)
            self.__thread.start()

    def get_list(self):
        if self.__list is None:
            return []
        else:
            return self.__list

    def show_animation(self):
        self.__list = deepcopy(self.__list)
        self.__algorithm = deepcopy(self.__algorithm)
        if self.__sort_control is not None:
            self.__sort_control.end()
        self.__sort_control = SortingController(self.__window, self.__list, self.__algorithm, sleeptime=0.25)
        self.__sort_control.start()
        self.__sort_control.end()



    def show_lists(self):
        self.__list_control = ListController(self.__window, self)

    def __get_a_key(self, dictionary):
        for key in dictionary.keys():
            return key

mc = MainController()
mc.start()