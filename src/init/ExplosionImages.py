from tkinter import *

class ExplosionImages:
    def getExplosionImages(self):
        explosion = []
        for i in range(5):
            file_name = "explosion" + str(i+1) + ".gif"
            explosion.append(PhotoImage(file="../pic/" + file_name))
        return explosion