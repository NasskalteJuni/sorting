from view.MainGui import MainWindow
from controller.ListEditController import ListController
from controller.SortingController import SortingController
from tkinter import Tk
from sorting.bubblesort import bubblesort
from sorting.pancakesort import pancakesort
from sorting.cocktailsort import cocktailsort
from sorting.whirlpoolsort import whirlpoolsort
from sorting.quicksort import quicksort
from sorting.shellsort import shellsort
from sorting.bogosort import bogosort
from sorting.combsort import combsort
from sorting.cyclesort import cyclesort
from sorting.insertionsort import insertionsort
from sorting.mergesort import iterative_mergesort
from sorting.gnomesort import gnomesort
from sorting.heapsort import heapsort
from sorting.selectionsort import selectionsort
from sorting.slowsort import slowersort
from time import sleep


def do_work():
    while True:
        sleep(1)
        print("working!")


class MainController:

    __algorithm_dictionary = None
    __algorithm = None
    __list = None
    __window = None
    __gui = None
    __list_control = None
    __sort_control = None


    def __init__(self, window):
        self.__init_window__(window)
        self.__algorithm_dictionary = {
            "bubble sort": bubblesort,
            "pancake sort": pancakesort,
            "cocktail sort": cocktailsort,
            "merge sort": iterative_mergesort,
            "whirlpool sort": whirlpoolsort,
            "quick sort": quicksort,
            "gnome sort": gnomesort,
            "heap sort": heapsort,
            "selection sort": selectionsort,
            "shell sort": shellsort,
            "bogo sort": bogosort,
            "comb sort": combsort,
            "cycle sort": cyclesort,
            "insertion sort": insertionsort,
            "slow sort": slowersort
        }

    def start(self):
        if self.__gui is not None:
            self.__gui.show_menu(self.__algorithm_dictionary)
            self.__window.mainloop()

    def set_algorithm(self, algorithm):
        if algorithm is not None:
            self.__algorithm = algorithm
        self.restart_animation()

    def get_algorithm(self):
        return self.__algorithm

    def set_list(self, input_list):
        if input_list is not None and len(input_list) > 0:
            self.__list = input_list
        self.restart_animation()

    def get_list(self):
        if self.__list is None:
            return []
        else:
            return self.__list

    def start_animation(self):
        print("started animation")
        self.__sort_control = SortingController(self.__window, self.__list, self.__algorithm, 0.5)
        self.__sort_control.start()

    def restart_animation(self):
        self.stop_animation()
        self.start_animation()

    def stop_animation(self):
        print("stopped animation")
        if self.__sort_control is not None:
            self.__sort_control.end()
            self.__sort_control = None

    def show_lists(self):
        if self.__sort_control is not None:
            self.__sort_control.end()
        self.__list_control = ListController(self.__window, self)

    def __get_a_key(self, dictionary):
        for key in dictionary.keys():
            return key

    def __init_window__(self, window=None):
        self.__window = window
        self.__gui = MainWindow(self.__window, self)
