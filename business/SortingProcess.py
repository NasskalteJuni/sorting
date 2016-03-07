from multiprocessing import Process, Pipe
from multiprocessing import ProcessError
from threading import Thread, Event
from observable.observablelist import ObservableList
from observable.observer import Observer
import psutil
from time import sleep


EOF = "EOF"


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


# what the process does -> observe the list while it is being sorted,
# send everytime the current state is notified this state through the given pipe
def observed_sorting(algorithm, sortable_list, pipe, sleeptime=None):
    in_copy_detector = InCopyDetector(sortable_list)
    sleeptime = 0.5 if sleeptime is None else sleeptime

    def send_timed_state(state):
        if not in_copy_detector.has_copy_clone(state):
            pipe.send(state)
            sleep(sleeptime)
        else:
            sleep(sleeptime/5)

    observable = ObservableList(seq=sortable_list)
    observer = Observer(send_timed_state)
    observable.add_observer(observer)
    algorithm(observable)
    pipe.send(EOF)


# listening to the things the process sends through the pipe,
# giving them to the given callback function
def listening(callback, pipe, event):
    received = None
    while event.isSet() and received != EOF:
        try:
            received = pipe.recv()
        except EOFError:
            print("already closed sorting process")
        if received != EOF:
            callback(received)


class SortingProcess:
    __event = None
    __process = None
    __listener = None
    __pipe = None

    def __init__(self, algorithm, sortable_list, on_sort_callback, sleeptime, name="running_sorting_algorithm"):
        self.__event = Event()
        self.__pipe, process_end_pipe = Pipe()
        self.__listener = Thread(target=listening, args=(on_sort_callback, self.__pipe, self.__event))
        self.__process = Process(target=observed_sorting, args=(algorithm, sortable_list, process_end_pipe, sleeptime))
        self.__process.name = name

    def start(self):
        self.__event.set()
        if self.__process is not None and self.__pipe is not None and not self.__process.is_alive():
            try:
                self.__process.daemon = True
                self.__listener.setDaemon(True)
                self.__listener.start()
                self.__process.start()
                self.__process.join()
            except ProcessError:
                print("Error starting the process")

    def stop(self):
        self.__event.clear()
        for proc in psutil.process_iter():
            if proc.name == self.__process.name:
                try:
                    proc.kill()
                except ProcessError:
                    print("Error stopping the process")
        if self.__pipe is not None:
            self.__pipe.close()
