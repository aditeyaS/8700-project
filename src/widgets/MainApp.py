import tkinter as tk

import const.app_config as AppConfig

class MainApp(tk.Tk):
    __instance = None

    @staticmethod
    def getInstance():
        if MainApp.__instance == None:
            MainApp()
        return MainApp.__instance

    def __init__(self):
        if MainApp.__instance != None:
            raise Exception("Singleton class")
        else:
            MainApp.__instance = self

    def __init__(self, *args, **kwargs):
        if MainApp.__instance != None:
            raise Exception("Singleton class")
        else:
            MainApp.__instance = self
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(f"{AppConfig.WINDOW_WIDTH}x{AppConfig.WINDOW_HEIGHT}")
        self.title(f"{AppConfig.GAME_NAME}")
        self.resizable(False, False)
        icon = tk.PhotoImage(file="../pic/icon.gif")
        self.iconphoto(False, icon)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)