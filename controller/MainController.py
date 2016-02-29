from view.MainGui import MainWindow
from controller.ListEditController import ListController
from tkinter import Tk
from sorting.bubblesort import bubblesort
from sorting.pancakesort import pancakesort
from sorting.cocktailsort import cocktailsort

class MainController:

    __algorithm_dictionary = None
    __algorithm = None
    __list = None
    __window = None
    __gui = None

    def __init__(self):
        self.__window = Tk()
        self.__window.title("SortingAlgorithms at work")
        self.__window.geometry("500x450")
        self.__window.resizable(0,0)
        self.__window.configure(bg="#222")
        self.__gui = MainWindow(self.__window, self)
        self.__algorithm_dictionary = {"bubble sort" : bubblesort, "pancake sort" : pancakesort, "cocktail sort" : cocktailsort}

    def start(self):
        self.__gui.show_menu(self.__algorithm_dictionary)
        self.__window.mainloop()

    def set_algorithm(self, algorithm):
        if algorithm is not None:
            self.__algorithm = algorithm

    def get_algorithm(self):
        return self.__algorithm

    def set_list(self, input_list):
        if input_list is not None and len(input_list) > 0:
            self.__list = input_list

    def get_list(self):
        if self.__list is None:
            return []
        else:
            return self.__list

    def show_animation(self):
        pass

    def show_lists(self):
        list_control = ListController(self.__window, self)

mc = MainController()
mc.start()