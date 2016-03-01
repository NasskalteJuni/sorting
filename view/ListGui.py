from tkinter import *


class ListWindow:

    __main_controller = None
    __window = None
    __list = None
    __min_var = None
    __max_var = None
    __list_string_var = None
    __menu = None

    def __init__(self, window, main_controller):
        self.__window = window
        self.__main_controller = main_controller
        self.__list = self.__main_controller.get_list()
        self.__min_var = IntVar()
        self.__min_var.set(0)
        self.__max_var = IntVar()
        self.__max_var.set(15)
        self.__list_string_var = StringVar()
        self.__list_string_var.set(self.__create_input_from_list(self.__main_controller.get_list()))

    def show_list_edit(self):
        self.__menu = Frame(self.__window)
        self.__menu.configure()
        self.__menu.pack(fill=BOTH, expand=True)
        line1 = Frame(self.__menu)
        line1.pack(side=TOP, fill=X, expand=False, padx=5, pady=15)
        near_sorted_btn = Button(line1, command=self.__main_controller.create_nearly_sorted_list)
        near_sorted_btn.configure(text="create nearly sorted list", command=self.__create_nearly_sorted_list)
        near_sorted_btn.pack(side=LEFT)
        true_random_btn = Button(line1)
        true_random_btn.configure(text="create random list", command=self.__create_absolutely_random_list)
        true_random_btn.pack(side=LEFT)
        min_field = Spinbox(line1, from_=1, to=15)
        min_field.configure(textvariable=self.__min_var)
        min_field.pack(side=LEFT)
        max_field = Spinbox(line1, from_=1, to=15)
        max_field.configure(textvariable=self.__max_var)
        max_field.pack(side=LEFT)
        line2 = Frame(self.__menu)
        line2.pack(side=TOP,fill=X, expand=False, padx=5, pady=15)
        list_field = Entry(line2)
        list_field.configure(textvariable=self.__list_string_var)
        list_field.pack(fill=X)
        line3 = Frame(self.__menu)
        line3.pack(fill=X, expand=False, padx=5, pady=15)
        submit_btn = Button(line3)
        submit_btn.configure(text="submit", command=self.submit)
        submit_btn.pack(side=TOP)
        information = Text(self.__menu)
        information.insert(END, "You can enter a list of numbers that should be sorted into the input field. \
Use a ';' to separate them. \
You can also generate nearly sorted or absolutely random lists with the buttons above,\
The fields beside them let you enter the minimal and maximal value of the generated list.\
By clicking on 'Submit', the list in the inputfield becomes the list to sort and the animation starts")
        information.configure(state=DISABLED, relief=FLAT, wrap=WORD)
        information.pack(side=BOTTOM, fill=X, padx=5, pady=10)

    def submit(self):
        if self.__list_string_var.get() is not None and len(self.__create_list_with_input(self.__list_string_var.get())) > 0:
            self.__main_controller.back_to_animation()
            self.__main_controller.set_list(self.__create_list_with_input(self.__list_string_var.get()))

    def hide_list(self):
        if self.__menu is not None:
            self.__menu.destroy()

    def __create_nearly_sorted_list(self):
        new_list = self.__main_controller.create_nearly_sorted_list(min_value=self.__min_var.get(), max_value=self.__max_var.get())
        self.__list_string_var.set(self.__create_input_from_list(new_list))

    def __create_absolutely_random_list(self):
        new_list = self.__main_controller.create_absolutely_random_list(min_value=self.__min_var.get(), max_value=self.__max_var.get())
        self.__list_string_var.set(self.__create_input_from_list(new_list))

    def __create_list_with_input(self, input_string) -> list:
        input_list = [x.strip() for x in input_string.split(';')]
        for i in range(0, len(input_list)):
            if input_list[i] is None or input_list[i] == "":
                del input_list[i]
            else:
                try:
                    input_list[i] = int(input_list[i])
                except TypeError:
                    input_list[i] = 0
        return input_list

    def __create_input_from_list(self, input_list) -> str:
        if input_list is None:
            input_list = []
        last = len(input_list)-1
        tmp_string = ""
        for x in range(0, len(input_list)):
            tmp_string += str(input_list[x])+ ";" if x != last else str(input_list[x])
        return tmp_string

