from view.AlgorithmGui import AlgorithmGui

algorithm = None

class AlgorithmController:

    def __init__(self, window, main_controller):
        self.__window = window
        self.__main_controller = main_controller
        self.__gui = None

    def show_edit(self):
        if self.__gui is None:
            self.__gui = AlgorithmGui(self.__window, self)
        self.__gui.show_form()

    def hide_edit(self):
        if self.__gui is not None:
            self.__gui.hide_form()

    def create_algorithm(self, alg_string):
        global algorithm
        alg_string = "from sorting.algorithmlist import sorting_algorithm \nglobal algorithm \n"+alg_string
        exec(alg_string)
        user_algorithm = algorithm
        print(algorithm)
        self.__main_controller.init_user_algorithm(user_algorithm)
        self.hide_edit()
        self.__gui = None
