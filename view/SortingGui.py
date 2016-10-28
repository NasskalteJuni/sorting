from tkinter import Canvas, TclError
from colorsys import hsv_to_rgb
from view.StyleGuide import *


class SortingAnimation:

    __window = None
    __canvas = None
    __canvas_width = 500
    __canvas_height = 450
    __interpolate = None
    __bar_dict = None
    __dict = {}

    def __init__(self, window):
        self.__window = window
        self.__canvas = Canvas(self.__window,
                               height=self.__canvas_height,
                               width=self.__canvas_width,
                               relief="ridge",
                               bd=0,
                               highlightthickness=0,
                               bg=gray)
        self.__canvas.pack()
        self.__interpolate = self.__make_interpolater(0, self.__canvas_height, 0, 1)

    def draw_list(self, drawable_list):
        if drawable_list is not None and len(drawable_list) > 0:
            rectangle_width = self.__canvas_width / len(drawable_list)
            rectangle_height = self.__canvas_height / (max(drawable_list))
            try:
                for i in range(0, len(drawable_list)):
                    x0 = rectangle_width*i
                    x1 = rectangle_width*i + rectangle_width
                    y0 = self.__canvas_height - (rectangle_height * int(drawable_list[i]))
                    y1 = self.__canvas_height
                    if self.__dict.get(x0) is not None:
                        self.__canvas.delete(self.__dict[x0])
                    self.__dict[x0] = self.__canvas.create_rectangle(x0, y0, x1, y1, fill=self.__get_bar_color(y0))
            except TclError:
                print("dirty gui update")

        self.__canvas.update()

    def hide_list(self):
        if self.__canvas is not None:
            self.__canvas.destroy()

    def __get_bar_color(self, height: float):
        height = 1.0 if height == 0.0 else height
        rgb = list(hsv_to_rgb(self.__interpolate(height), 1, 1))
        rgb[0] *= 255
        rgb[1] *= 255
        rgb[2] *= 255
        rgb = tuple([int(rgb[0]), int(rgb[1]), int(rgb[2])])
        return '#%02x%02x%02x' % rgb

    @staticmethod
    def __make_interpolater(left_min, left_max, right_min, right_max):
        left_span = left_max - left_min
        right_span = right_max - right_min
        scale_factor = float(right_span) / float(left_span)

        def interp_fn(value):
            return right_min + (value-left_min)*scale_factor

        return interp_fn
