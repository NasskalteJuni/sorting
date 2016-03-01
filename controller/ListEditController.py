from math import ceil
from random import randint
from view.ListGui import ListWindow


class ListController:

    __gui = None
    __main_controller = None
    __list = None

    def __init__(self, window, main_controller):
        self.__main_controller = main_controller
        self.window = window
        self.__gui = ListWindow(window, self)
        self.__gui.show_list_edit()

    def create_nearly_sorted_list(self, min_value, max_value, reversed=False):
        reverse = reversed
        if min_value > max_value:
            reverse = not reverse
            min_value, max_value = max_value, min_value
        tmp_list = []
        for x in range(min_value, max_value):
            tmp_list.append(min_value+x)
        number_of_random_swaps = ceil((max_value-min_value)/10)
        for x in range(0, number_of_random_swaps):
            rnd1 = randint(0, len(tmp_list)-1)
            rnd2 = randint(0, len(tmp_list)-1)
            tmp_list[rnd1], tmp_list[rnd2] = tmp_list[rnd2], tmp_list[rnd1]
        if reverse:
            tmp_list.reverse()
        self.__list = tmp_list
        return self.__list

    def create_absolutely_random_list(self, min_value, max_value):
        def insert_in_empty_place(some_list, index, value):
            i = index if index < len(some_list) else index % len(some_list)
            while some_list[i] is not None:
                i = i+1 if i+1 < len(some_list) else 0
                if i == index:
                    some_list.append(value)
                    break
            some_list[i] = value

        if min_value > max_value:
            min_value, max_value = max_value, min_value
        tmp_list = [None for x in range(min_value, max_value)]
        for x in range(min_value, max_value):
            insert_in_empty_place(tmp_list, randint(min_value, max_value), x)
        for i in range(0, len(tmp_list)):
            if tmp_list[i] is None:
                del tmp_list[i]
        self.__list = tmp_list
        return self.__list

    def set_list(self, input_list):
        self.__main_controller.set_list(input_list)

    def get_list(self):
        self.__main_controller.get_list()

    def back_to_animation(self):
        self.__gui.hide_list()
        self.__main_controller.show_animation()
