from view.MainGui import MainWindow
from controller.ListEditController import ListController
from controller.SortingController import SortingController
from sorting.bubblesort import bubblesort
from sorting.pancakesort import pancakesort
from sorting.cocktailsort import cocktailsort
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
from threading import Thread


# The main controller that is a central node which coordinates different sub-controllers and tells them what to do
class MainController:

    __sort_control = None
    __list_control = None

    def __init__(self, window):
        self.__init_window__(window)
        self.__algorithm_dictionary = {
            "bubble sort": bubblesort,
            "pancake sort": pancakesort,
            "cocktail sort": cocktailsort,
            "merge sort": iterative_mergesort,
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
        self.__algorithm = self.__algorithm_dictionary[self.__get_a_key(self.__algorithm_dictionary)]
        self.__list = [1, 8, 7, 10, 9, 3, 2, 5, 6, 4]
        self.__sleeptime = 0.5

    def start(self):
        if self.__gui is not None:
            self.__gui.show_menu(self.__algorithm_dictionary)
            self.restart_animation()
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

    def set_sleeptime(self, sleeptime):
        self.__sleeptime = sleeptime
        self.restart_animation()

    def start_animation(self):
        print("started animation")
        self.__sort_control = SortingController(self.__window, self.__list, self.__algorithm, self.__sleeptime)
        self.__sort_control.start()

    def restart_animation(self):
        def inner_func():
            self.stop_animation()
            self.start_animation()
        t = Thread(target=inner_func, args=())
        t.setDaemon(True)
        t.start()

    def stop_animation(self):
        print("stopped animation")
        if self.__sort_control is not None:
            self.__sort_control.end()
            self.__sort_control = None

    def show_lists(self):
        if self.__sort_control is not None:
            self.__sort_control.end()
        self.__list_control = ListController(self.__window, self)

    @staticmethod
    def __get_a_key(dictionary):
        for key in dictionary.keys():
            return key

    def __init_window__(self, window=None):
        self.__window = window
        self.__gui = MainWindow(self.__window, self)
