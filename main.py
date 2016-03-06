
#launch script, do not try to import this
# (if you import it, it will do nothing - import the classes instead)
if __name__ == '__main__':
    from controller.MainController import MainController
    from tkinter import Tk

    window = Tk()

    mc = MainController(window)
    mc.start()
