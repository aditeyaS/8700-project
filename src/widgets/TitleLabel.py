import tkinter as tk

import const.colors as Colors

class TitleLabel(tk.Label):
    def __init__(self, parent, text):
        tk.Label.__init__(
            self,
            parent,
            text=text,
            background=Colors.BLACK,
            foreground=Colors.BABY_BLUE,
            font='Arial 25 bold',
            padx=20,
            pady=40,
        )
        self.grid(row=0, column=0)