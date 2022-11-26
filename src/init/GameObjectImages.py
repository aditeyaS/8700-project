from tkinter import PhotoImage

import const.app_config as AppConfig

class GameObjectImages:
    def getBlue(self):
        blue_evil_spirits = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "blue_" + d + ".gif"
            blue_evil_spirits[d] = PhotoImage(file="../pic/devil/" + fileName)
        return blue_evil_spirits

    def getBlack(self):
        black_evil_spirits = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "black_" + d + ".gif"
            black_evil_spirits[d] = PhotoImage(file="../pic/devil/" + fileName)
        return black_evil_spirits

    def getRed(self):
        red_evil_spirits = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "red_" + d + ".gif"
            red_evil_spirits[d] = PhotoImage(file="../pic/devil/" + fileName)
        return red_evil_spirits

    def getPlayer(self):
        pumpkin = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "pumpkin_" + d + ".gif"
            pumpkin[d] = PhotoImage(file="../pic/player/" + fileName)
        return pumpkin

    def getAll(self):
        game_object_images = {}
        game_object_images["blue"] = self.getBlue()
        game_object_images["black"] = self.getBlack()
        game_object_images["red"] = self.getRed()
        game_object_images["pumpkin"] = self.getPlayer()
        return game_object_images
