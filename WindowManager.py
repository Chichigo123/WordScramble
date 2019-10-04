import tkinter as tk

HEIGHT = 0
WIDTH = 1
class BaseWindowManager():
    """
    This is base class of Window
    """

    def __init__(self, config):
        self.createWindow(config.windowConfig)

    def createWindow(self, windowConfig):
        window = tk.Tk(windowConfig.get('screenName'),  windowConfig.get('baseName'),  windowConfig.get('className'),
                       windowConfig.get('useTk'))
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        w = windowConfig.get('geometry')[WIDTH]
        h = windowConfig.get('geometry')[HEIGHT]
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        window.resizable(0, 0)
        window.geometry("%dx%d+%d+%d" % (w, h, x, y))

        window.configure(bg = windowConfig.get('bg'))
        return window

class DerivedWindowManager(BaseWindowManager):
    """
    This is derived class of Window
    """

    def __init__(self, config):
        self.window = self.createWindow(config.windowConfig)

