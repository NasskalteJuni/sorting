from time import sleep

from business.SortingProcess import SortingProcess
from observable import observablelist
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
    __sortlist = observablelist.ObservableList()
    __sortalgorithm = None
    __sleeptime = 1
    __gui = None
    __in_copy_process_detector = None
    __process = None
    __stopped = True

    def __init__(self, window, sortlist, sortalgorithm, sleeptime=1.0):
        if sortlist is None:
            sortlist = []
        self.__gui = SortingAnimation(window)
        self.__sortalgorithm = sortalgorithm
        self.__sleeptime = sleeptime
        self.__in_copy_process_detector = InCopyDetector(sortlist)
        self.__sortlist = observablelist.ObservableList()
        for x in sortlist:
            self.__sortlist.append(x)
        self.__sortlist.add_observer(self)
        self.__process = SortingProcess(self.__sortalgorithm, self.__sortlist, self.notify)

    def start(self):
        self.__process.start()
        self.__stopped = False

    def end(self):
        self.__process.stop()
        print("called end")
        if self.__gui is not None:
            self.destroy_gui()
        self.__stopped = True

    def notify(self, unsorted_list):
        print("unsorted_list: "+str(unsorted_list))
        if not self.__stopped:
            if not self.__in_copy_process_detector.has_copy_clone(unsorted_list):
                self.__gui.draw_list(list(unsorted_list))

    def destroy_gui(self):
        self.__gui.hide_list()
        self.__gui = None



# algorithms = [bubblesort, combsort, cocktailsort, gnomesort, shellsort, iterative_mergesort, cyclesort, quicksort, heapsort, selectionsort, insertionsort, pancakesort, bogosort]
# sc = SortingController([13, 1, 12, 7, 4, 5, 11, 9, 2, 8, 15, 3, 6, 10, 14], algorithms[7], 0.75)
# sc.start()
