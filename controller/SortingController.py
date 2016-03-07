from business.SortingProcess import SortingProcess
from view.SortingGui import SortingAnimation


class SortingController:

    def __init__(self, window, sortlist, sortalgorithm, sleeptime=1.0):
        if sortlist is None:
            sortlist = []
        self.__gui = SortingAnimation(window)
        self.__sortalgorithm = sortalgorithm
        self.__sleeptime = sleeptime
        self.__sortlist = sortlist
        self.__process = SortingProcess(self.__sortalgorithm, self.__sortlist, self.notify, sleeptime=sleeptime)

    def start(self):
        self.__process.start()

    def end(self):
        self.__process.stop()
        if self.__gui is not None:
            self.destroy_gui()

    def notify(self, unsorted_list):
        self.__gui.draw_list(unsorted_list)

    def destroy_gui(self):
        self.__gui.hide_list()
        self.__gui = None
