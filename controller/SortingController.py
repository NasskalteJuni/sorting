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

class SortingController:

    __sortlist = observablelist.ObservableList()
    __sortalgorithm = None
    __sleeptime = 1
    __gui = Gui()
    __model_animation_queue = Queue()

    def start(self):
        self.__gui.create()
        self.__gui.run()
        sleep(self.__sleeptime)
        self.__sortalgorithm(self.__sortlist)

    def notify(self, unsorted_list):
        self.__model_animation_stack.put(unsorted_list)

    def draw(self, unsorted_list):
        self.__gui.set_list(unsorted_list)

    def __init__(self, sortlist, sortalgorithm, sleeptime=1):
        if sortlist is None:
            sortlist = []
        self.__model_animation_queue = Queue()
        self.__sortalgorithm = sortalgorithm
        self.__sleeptime = sleeptime
        self.__sortlist = observablelist.ObservableList()
        for x in sortlist:
            self.__sortlist.append(x)
        self.__sortlist.add_observer(self)

sc = SortingController([1, 7, 4, 5, 9, 2, 1, 3, 6], mergesort, 0.5)
sc.start()
