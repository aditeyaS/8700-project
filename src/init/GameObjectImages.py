from tkinter import PhotoImage

import const.app_config as AppConfig

class GameObjectImages:
    def getBlue(self):
        tank = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "blue_" + d + ".gif"
            tank[d] = PhotoImage(file="../pic/devil/" + fileName)
        return tank

    def getBlack(self):
        tank = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "black_" + d + ".gif"
            tank[d] = PhotoImage(file="../pic/devil/" + fileName)
        return tank

    def getRed(self):
        tank = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "red_" + d + ".gif"
            tank[d] = PhotoImage(file="../pic/devil/" + fileName)
        return tank

    def getPlayer(self):
        tank = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "pumpkin_" + d + ".gif"
            tank[d] = PhotoImage(file="../pic/player/" + fileName)
        return tank

    def getAll(self):
        game_object_images = {}
        game_object_images["blue"] = self.getBlue()
        game_object_images["black"] = self.getBlack()
        game_object_images["red"] = self.getRed()
        game_object_images["huge"] = self.getPlayer()
        return game_object_images
