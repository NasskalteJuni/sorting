from multiprocessing import freeze_support

# launch script, do not try to import this
# (if you import it, it will do nothing - import the classes instead)
if __name__ == '__main__':
    freeze_support()
    from controller.MainController import MainController
    from tkinter import Tk

    window = Tk()

    mc = MainController(window)
    mc.start()
