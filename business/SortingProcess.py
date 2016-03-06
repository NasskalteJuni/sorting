from multiprocessing import Process
from multiprocessing import ProcessError
import psutil



class ProcessDummy:

    __process = None
    __target = None

    def __init__(self, target, args=(), name="running_sorting_algorithm"):
        print("created process...")
        self.__target = target
        self.__process = Process(target=self.__target, args=args)
        self.__process.name = name

    def start(self):
        print("started process")
        if self.__process is not None and self.__target is not None and not self.__process.is_alive():
            try:
                self.__process.daemon = True
                self.__process.start()
                self.__process.join()
            except ProcessError:
                print("Error starting the process")

    def stop(self):
        print("stopped process")
        for proc in psutil.process_iter():
            if proc.name == self.__process.name:
                try:
                    proc.kill()
                except ProcessError:
                    print("Error stopping the process")

