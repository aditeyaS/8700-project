from tkinter import *

import const.app_config as AppConfig

class BulletImages:
    def getBlue(self):
        bullet = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "bullet_" + d + ".gif"
            bullet[d] = PhotoImage(file="../pic/devil/" + fileName)
        return bullet

    def getBlack(self):
        bullet = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "bullet_" + d + ".gif"
            bullet[d] = PhotoImage(file="../pic/devil/" + fileName)
        return bullet

    def getRed(self):
        bullet = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "bullet_" + d + ".gif"
            bullet[d] = PhotoImage(file="../pic/devil/" + fileName)
        return bullet

    def getPlayer(self):
        bullet = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "bullet_" + d + ".gif"
            bullet[d] = PhotoImage(file="../pic/player/" + fileName)
        return bullet

    def getAll(self):
        bullet_images = {}
        bullet_images["blue"] = self.getBlue()
        bullet_images["black"] = self.getBlack()
        bullet_images["red"] = self.getRed()
        bullet_images["huge"] = self.getPlayer()
        return bullet_images
