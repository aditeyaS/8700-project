import tkinter as tk

import const.app_config as AppConfig
import const.colors as Colors

class PageFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(
            self,
            parent,
            height=AppConfig.WINDOW_HEIGHT,
            width=AppConfig.WINDOW_WIDTH,
            bg=Colors.BLACK
        )
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        