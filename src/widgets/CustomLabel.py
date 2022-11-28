import tkinter as tk

import const.colors as Colors

class CustomLabel(tk.Label):
    def __init__(self, parent, text, color=None):
        tk.Label.__init__(
            self,
            parent,
            text=text,
            background=Colors.BLACK,
            foreground= color if color else Colors.WHITE,
            font='Arial 16',
            padx=20,
            pady=20,
        )