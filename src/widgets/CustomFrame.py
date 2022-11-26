import tkinter as tk

import const.colors as Colors

class CustomFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(
            self,
            parent,
            bg=Colors.BLACK
        )        