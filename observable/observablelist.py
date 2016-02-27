
class ObservableList(list):

    __observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def get_observers(self):
        return self.__observers

    def set_observers(self, observers):
        self.__observers = observers

    def notify_observers(self):
        for observer in self.__observers:
            observer.notify(self)

    # def append(self, p_object):
    #     tmp = super(ObservableList, self).append(p_object)
    #     self.notify_observers()
    #     return tmp
    #
    # def extend(self, iterable):
    #     tmp = super(ObservableList, self).extend(iterable)
    #     self.notify_observers()
    #     return tmp
    #
    # def insert(self, index, p_object):
    #     tmp = super(ObservableList, self).insert(index, p_object)
    #     self.notify_observers()
    #     return tmp
    #
    # def pop(self, index=None):
    #     tmp = super(ObservableList, self).pop(index)
    #     self.notify_observers()
    #     return tmp
    #
    # def remove(self, value):
    #     tmp = super(ObservableList, self).remove(value)
    #     self.notify_observers()
    #     return tmp
    #
    # def reverse(self):
    #     tmp = super(ObservableList, self).reverse()
    #     self.notify_observers()
    #     return tmp
    #
    # def sort(self, key=None, reverse=False):
    #     tmp = super(ObservableList, self).sort(key, reverse)
    #     self.notify_observers()
    #     return tmp

    def __add__(self, y):
        tmp = super(ObservableList, self).__add__(y)
        self.notify_observers()
        return tmp

    def __delitem__(self, y):
        tmp = super(ObservableList, self).__delitem__(y)
        self.notify_observers()
        return tmp

    def __iadd__(self, y):
        tmp = super(ObservableList, self).__iadd__(y)
        self.notify_observers()
        return tmp

    def __imul__(self, y):
        tmp = super(ObservableList, self).__imul__(y)
        self.notify_observers()
        return tmp


    def __init__(self, seq=()):  # known special case of list.__init__
        tmp = super(ObservableList, self).__init__(seq)
        self.notify_observers()
        return tmp

    def __mul__(self, n):
        tmp = super(ObservableList, self).__mul__(n)
        self.notify_observers()
        return tmp

    def __reversed__(self):
        tmp = super(ObservableList, self).__reversed(self)
        self.notify_observers()
        return tmp

    def __rmul__(self, n):
        tmp = super(ObservableList, self).__rmul__(n)
        self.notify_observers()
        return tmp

    def __setitem__(self, i, y):
        tmp = super(ObservableList, self).__setitem__(i, y)
        self.notify_observers()
        return tmp
