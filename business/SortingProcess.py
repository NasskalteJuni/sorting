from multiprocessing import Process, Pipe
from multiprocessing import ProcessError
from threading import Thread, Event
from observable.observablelist import ObservableList
from observable.observer import Observer
import psutil
from time import sleep


EOF = "EOF"


# what the process does -> observe the list while it is being sorted,
# send everytime the current state is notified this state through the given pipe
def observed_sorting(algorithm, sortable_list, pipe, sleeptime=None):
    sleeptime = 0.5 if sleeptime is None else sleeptime

    def send_timed_state(state):
        pipe.send(state)
        sleep(sleeptime)

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
        received = pipe.recv()
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
                self.__listener.start()
                self.__process.start()
                self.__process.join()
            except ProcessError:
                print("Error starting the process")

    def stop(self):
        self.__event.clear()
        if self.__pipe is not None:
            self.__pipe.close()
        for proc in psutil.process_iter():
            if proc.name == self.__process.name:
                try:
                    proc.kill()
                except ProcessError:
                    print("Error stopping the process")
