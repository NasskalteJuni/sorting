from time import sleep
from view.SortingGui import SortingAnimation
from observable import observablelist
from threading import Thread


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
    __thread = None
    __stopped = False

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
        self.__stopped = False

    def start(self):
        try:
            self.__thread = Thread(target=self.__sortalgorithm, args=(self.__sortlist,))
            self.__thread.setDaemon(True)
            self.__thread.start()
        except:
            print("An exception occurred during the sorting process")

    def end(self):
        self.kill_sorting_thread()
        print("called end")
        if self.__gui is not None:
            self.destroy_gui()
        self.__sortlist = None
        self.__sortalgorithm = None
        self.__thread = None
        self.__stopped = True

    def notify(self, unsorted_list):
        if not self.__stopped:
            if not self.__in_copy_process_detector.has_copy_clone(unsorted_list):
                self.__gui.draw_list(unsorted_list)
                sleep(self.__sleeptime)

    def destroy_gui(self):
        self.__gui.hide_list()
        self.__gui = None

    def kill_sorting_thread(self):
        if self.__thread is not None:
            self.__thread._delete()
            self.__thread = None

# algorithms = [bubblesort, combsort, cocktailsort, gnomesort, shellsort, iterative_mergesort, cyclesort, quicksort, heapsort, selectionsort, insertionsort, pancakesort, bogosort]
# sc = SortingController([13, 1, 12, 7, 4, 5, 11, 9, 2, 8, 15, 3, 6, 10, 14], algorithms[7], 0.75)
# sc.start()
