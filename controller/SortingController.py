from time import sleep
from view.gui import Gui
from sorting.bubblesort import bubblesort
from sorting.selectionsort import selectionsort
from sorting.heapsort import heapsort
from sorting.bogosort import bogosort
from sorting.gnomesort import gnomesort
from sorting.insertionsort import insertionsort
from sorting.bucketsort import bucketsort
from queue import Queue
from sorting.mergesort import mergesort
from observable import observablelist
from threading import Thread


class SortingThread(Thread):

    def get_id(self):
        return self.__threadID

    def __init__(self, threadID, sortable_list, sorting_algorithm):
        self.__threadID = threadID
        self.__sortable_list = sortable_list
        self.__sorting_algorithm = sorting_algorithm

    def run(self):
        print("run thread "+str(self.__threadID))
        self.__sorting_algorithm(self.__sortable_list)

class SortingController:

    __sortlist = observablelist.ObservableList()
    __sortalgorithm = None
    __sleeptime = 1
    __gui = None
    __model_animation_queue = []

    def start(self):
        s = SortingThread(threadID="t1", sortable_list=self.__sortlist, sorting_algorithm=self.__sortalgorithm)
        self.__gui.run(self.__model_animation_queue)
        # sleep(self.__sleeptime)
        # self.__sortalgorithm(self.__sortlist)

    def notify(self, unsorted_list):
        self.__model_animation_queue.append(unsorted_list)

    def draw(self, unsorted_list):
        self.__gui.set_list(unsorted_list)

    def __init__(self, sortlist, sortalgorithm, sleeptime=1):
        if sortlist is None:
            sortlist = []
        self.__model_animation_queue = []
        self.__sortalgorithm = sortalgorithm
        self.__sleeptime = sleeptime
        self.__sortlist = observablelist.ObservableList()
        for x in sortlist:
            self.__sortlist.append(x)
        self.__sortlist.add_observer(self)
        self.__gui = Gui()

sc = SortingController([1, 7, 4, 5, 9, 2, 1, 3, 6], mergesort, 0.5)
sc.start()
