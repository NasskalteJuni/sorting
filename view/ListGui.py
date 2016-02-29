from tkinter import *


class ListWindow:

    __main_contoller = None
    __window = None
    __list = None
    __min_var = None
    __max_var = None
    __list_string_var = None
    __menu = None

    def __init__(self, window, main_controller):
        self.__window = window
        self.__main_contoller = main_controller
        self.__list = self.__main_controller.get_list()
        self.__min_var = IntVar()
        self.__min_var.set(0)
        self.__max_var = IntVar()
        self.__max_var.set(15)
        self.__list_string_var = StringVar()
        self.__list_string_var.set(self.__create_input_from_list(self.__main_contoller.get_list()))

    def show_list_edit(self):
        self.__menu = Frame(self.__window)
        self.__menu.pack()
        line1 = Frame(self.__menu)
        line1.pack()
        near_sorted_btn = Button(line1, command=self.__main_contoller.create_nearly_sorted_list)
        near_sorted_btn.configure(label="create nearly sorted list", command=self.__create_nearly_sorted_list)
        near_sorted_btn.pack()
        true_random_btn = Button(line1)
        true_random_btn.configure(label="create random list", command=self.__create_absolutely_random_list)
        true_random_btn.pack()
        min_field = Spinbox(line1)
        min_field.configure(variable=self.__min_var)
        min_field.pack()
        max_field = Spinbox(line1)
        max_field.configure(variable=self.__max_var)
        max_field.pack()
        line2 = Frame(self.__menu)
        line2.pack()
        list_field = Entry(line2)
        list_field.configure(variable=self.__list_string_var)
        list_field.pack()
        line3 = Frame(self.__menu)
        line3.pack()
        submit_btn = Button(line3)
        submit_btn.configure(label="submit", command=self.submit)
        submit_btn.pack()

    def submit(self):
        self.__main_contoller.set_list(self.__create_list_with_input(self.__list_string_var.get()))
        self.__main_contoller.back_to_animation()

    def hide_list(self):
        if self.__menu is not None:
            self.__menu.destroy()

    def __create_nearly_sorted_list(self):
        new_list = self.__main_contoller.create_nearly_sorted_list(min_value=self.__min_var.get(), max_value=self.__max_var.get())
        self.__list_string_var.set(self.__create_input_from_list(new_list))

    def __create_absolutely_random_list(self):
        new_list = self.__main_contoller.create_absolutely_random_list(min_value=self.__min_var.get(), max_value=self.__max_var.get())
        self.__list_string_var.set(self.__create_input_from_list(new_list))

    def __create_list_with_input(self, input_string) -> list:
        input_list = [x.strip() for x in input_string.split(';')]
        for i in range(0, len(input_list)):
            if input_list[i] is None or input_list[i] == "":
                del input_list[i]
        return input_list

    def __create_input_from_list(self, input_list) -> str:
        last = len(input_list)-1
        tmp_string = ""
        for x in range(0, len(input_list)):
            tmp_string += str(input_list[x])+ ";" if x != last else str(input_list[x])
        return tmp_string

