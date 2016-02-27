import tkinter
import threading


class Gui:

    __framerate = 1
    __interval = int(1000 / __framerate)
    __window = tkinter.Tk()
    __canvas = None
    __canvas_width = 500
    __canvas_height = 450
    __list = []
    __animation_queue = None

    def __init__(self):
        self.create()

    def create(self):
        self.__window.title("SortingAlgorithms at work")
        self.__window.geometry("500x450")
        self.__canvas = tkinter.Canvas(self.__window, height=self.__canvas_height, width=self.__canvas_width, bg="white")
        self.__canvas.pack()

    def draw_list(self):
        print(self.__list)
        self.__canvas.delete("all")
        if self.__list is not None and len(self.__list) > 0:
            print(self.__list)
            rectangle_width = self.__canvas_width / len(self.__list)
            rectangle_height = self.__canvas_height / (max(self.__list))
            for i in range(0, len(self.__list)):
                x0 = rectangle_width*i
                x1 = rectangle_width*i + rectangle_width
                y0 = self.__canvas_height - (rectangle_height * int(self.__list[i]))
                y1 = self.__canvas_height
                self.__canvas.create_rectangle(x0, y0, x1, y1, fill="#000099")
        self.__canvas.update()

    def animate(self):
        if self.__animation_queue is not None and len(self.__animation_queue) > 0:
            self.__list = self.__animation_queue[0]
            del self.__animation_queue[0]
        print(self.__animation_queue)
        self.draw_list()
        self.__window.after(self.__interval, self.animate)

    def run(self, queue):
        self.__animation_queue = queue
        self.animate()
        self.__window.mainloop()


# def changelist():
#     gui.set_list(a_list)
#     gui.draw_list()
#     tmp = a_list[0]
#     a_list[0] = a_list[1]
#     a_list[1] = a_list[tmp]
#     gui.set_list(a_list)
#     gui.draw_list()
#
#
# gui = Gui()
# a_list = [1, 4, 3, 5, 7, 2, 8, 9, 6]
# gui.create()
# gui.run()


