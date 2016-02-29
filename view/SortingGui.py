import tkinter


class SortingAnimation:

    __framerate = 1
    __interval = int(1000 / __framerate)
    __window = None
    __canvas = None
    __canvas_width = 500
    __canvas_height = 450

    def __init__(self, window):
        self.__window = window
        self.__canvas = tkinter.Canvas(self.__window, height=self.__canvas_height, width=self.__canvas_width, bg="#FFF")
        self.__canvas.pack()

    def draw_list(self, drawable_list):
        self.__canvas.delete("all")
        if drawable_list is not None and len(drawable_list) > 0:
            rectangle_width = self.__canvas_width / len(drawable_list)
            rectangle_height = self.__canvas_height / (max(drawable_list))
            for i in range(0, len(drawable_list)):
                x0 = rectangle_width*i
                x1 = rectangle_width*i + rectangle_width
                y0 = self.__canvas_height - (rectangle_height * int(drawable_list[i]))
                y1 = self.__canvas_height
                self.__canvas.create_rectangle(x0, y0, x1, y1, fill="#000099")
        self.__canvas.update()

    def animate(self):
        self.__window.after(self.__interval, self.animate)

    def run(self):
        self.animate()
        self.__window.mainloop()
