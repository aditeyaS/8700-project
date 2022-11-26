import tkinter as tk

import const.colors as Colors
import const.app_config as AppConfig

def get_btn_color(btn_name) -> str:
    if btn_name == AppConfig.BTN_START:
        return Colors.GREEN
    elif btn_name == AppConfig.BTN_RESUME:
        return Colors.ORANGE
    else:
        return Colors.RED

class CustomButton(tk.Frame):
    def __init__(self, parent, text, command):
        btn_color = get_btn_color(text)
        tk.Button.__init__(
            self,
            parent,
            text=text,
            font=('Lithos Pro Regular', 15),
            padx=10,
            pady=10,
            command=command,
            width=18,
            bg=btn_color,
        )        