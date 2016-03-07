from tkinter import *


class AlgorithmGui:

    __form = None

    def __init__(self, window, main_controller):
        self.__window = window
        self.__main_controller = main_controller
        self.__form = None
        self.__text = None

    def show_form(self):
        self.__form = Frame(self.__window)
        self.__form.pack(fill=BOTH, expand=True)
        line1 = Frame(self.__form)
        line1.pack(fill=X, expand=False)
        self.__text = Text(line1)
        self.__text.insert(END, "# write your functions here. \n# place a '@sorting_algorithm' above your algorithm \n")
        self.__text.pack(fill=X, expand=True)
        line2 = Frame(self.__form)
        line2.pack(fill=X, side=BOTTOM, expand=True)
        submit_btn = Button(line2)
        submit_btn.configure(text="submit", command=self.submit)
        submit_btn.pack(fill=X, expand=True)

    def submit(self):
        if self.__text is not None:
            self.__main_controller.create_algorithm(self.__text.get(1.0, END))
            self.hide_form()

    def hide_form(self):
        if self.__form is not None:
            self.__form.destroy()
            self.__form = None
