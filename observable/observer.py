class Observer:

    __notify_callback = None
    __block_notify = False

    def __init__(self, notify_callback, block_notify=False):
        self.__notify_callback = notify_callback
        self.__block_notify = block_notify

    def notify(self, obj):
        if not self.__block_notify and self.__notify_callback is not None:
            self.__notify_callback(obj)

    def block_notify(self):
        self.__block_notify = True

    def toggle_notify_block(self):
        self.__block_notify = not self.__block_notify

    def set_notify_callback(self, callback):
        self.__notify_callback = callback