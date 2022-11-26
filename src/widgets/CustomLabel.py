import tkinter as tk

import const.colors as Colors

class CustomLabel(tk.Label):
    def __init__(self, parent, text):
        tk.Label.__init__(
            self,
            parent,
            text=text,
            background=Colors.BLACK,
            foreground=Colors.WHITE,
            font='Arial 16',
            padx=20,
            pady=20,
        )
        self.grid(row=0, column=0)