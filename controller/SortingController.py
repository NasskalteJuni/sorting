from business.SortingProcess import SortingProcess
from view.SortingGui import SortingAnimation


# just to not show the frames that have the swapping process
# (not in observable_list because this skipping does not belong to the observing process)
class InCopyDetector:

    def __init__(self, initial_list):
        self.__initial_list = initial_list

    def has_copy_clone(self, comparable_list):
        for x in range(0, len(self.__initial_list)):
            if self.__initial_list.count(x) != comparable_list.count(x):
                return True
        return False


class SortingController:

    def __init__(self, window, sortlist, sortalgorithm, sleeptime=1.0):
        if sortlist is None:
            sortlist = []
        self.__gui = SortingAnimation(window)
        self.__sortalgorithm = sortalgorithm
        self.__sleeptime = sleeptime
        print("the given sortlist was "+str(sortlist))
        self.__in_copy_process_detector = InCopyDetector(sortlist)
        self.__sortlist = sortlist
        self.__process = SortingProcess(self.__sortalgorithm, self.__sortlist, self.notify, sleeptime=sleeptime)

    def start(self):
        self.__process.start()

    def end(self):
        self.__process.stop()
        print("called end")
        if self.__gui is not None:
            self.destroy_gui()

    def notify(self, unsorted_list):
            if not self.__in_copy_process_detector.has_copy_clone(unsorted_list):
                self.__gui.draw_list(unsorted_list)

    def destroy_gui(self):
        self.__gui.hide_list()
        self.__gui = None
