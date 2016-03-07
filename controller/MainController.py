from view.MainGui import MainWindow
from controller.ListEditController import ListController
from controller.SortingController import SortingController
from controller.AlgorithmEditController import AlgorithmController
from threading import Thread
from sorting.algorithmlist import get_algorithmlist


# The main controller that is a central node which coordinates different sub-controllers and tells them what to do
class MainController:

    __sort_control = None
    __list_control = None
    __algorithm_control = None
    __user_algorithm = None

    def __init__(self, window):
        self.__init_window__(window)
        self.__algorithm_dictionary = get_algorithmlist()
        print(self.__algorithm_dictionary)
        self.__algorithm = self.__algorithm_dictionary[1][1]
        self.__list = [1, 11, 14, 15, 19, 8, 7, 10, 16, 17, 9, 3, 2, 5, 12, 18, 6, 4, 20, 13]
        self.__sleeptime = 0.25

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

    def __init_window__(self, window=None):
        self.__window = window
        self.__gui = MainWindow(self.__window, self)
