from time import sleep
from view.gui import Gui
from sorting.bubblesort import bubblesort
from sorting.selectionsort import selectionsort
from sorting.heapsort import heapsort
from sorting.bogosort import bogosort
from sorting.gnomesort import gnomesort
from sorting.insertionsort import insertionsort
from sorting.mergesort import mergesort
from observable import observablelist


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

    def __init__(self, sortlist, sortalgorithm, sleeptime=1.0):
        if sortlist is None:
            sortlist = []
        self.__gui = Gui()
        self.__sortalgorithm = sortalgorithm
        self.__sleeptime = sleeptime
        self.__in_copy_process_detector = InCopyDetector(sortlist)
        self.__sortlist = observablelist.ObservableList()
        for x in sortlist:
            self.__sortlist.append(x)
        self.__sortlist.add_observer(self)

    def start(self):
        self.__sortalgorithm(self.__sortlist)
        self.__gui.run()

    def notify(self, unsorted_list):
        if not self.__in_copy_process_detector.has_copy_clone(unsorted_list):
            self.__gui.draw_list(unsorted_list)
            sleep(self.__sleeptime)

algorithms = [bubblesort, gnomesort, mergesort, heapsort, selectionsort, insertionsort, bogosort]
sc = SortingController([1, 12, 7, 4, 5, 11, 9, 2, 8, 3, 6, 10], algorithms[6], 0.75)
sc.start()
