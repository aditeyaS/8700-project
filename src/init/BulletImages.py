from tkinter import *

import const.app as AppConfig

class BulletImages:
    def getBlue(self):
        bullet = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "bullet_blue_" + d + ".gif"
            bullet[d] = PhotoImage(file="../pic/" + fileName)
        return bullet

    def getBlack(self):
        bullet = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "bullet_black_" + d + ".gif"
            bullet[d] = PhotoImage(file="../pic/" + fileName)
        return bullet

    def getRed(self):
        bullet = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "bullet_red_" + d + ".gif"
            bullet[d] = PhotoImage(file="../pic/" + fileName)
        return bullet

    def getPlayer(self):
        bullet = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "bullet_huge_" + d + ".gif"
            bullet[d] = PhotoImage(file="../pic/" + fileName)
        return bullet

    def getAll(self):
        bullet_images = {}
        bullet_images["blue"] = self.getBlue()
        bullet_images["black"] = self.getBlack()
        bullet_images["red"] = self.getRed()
        bullet_images["huge"] = self.getPlayer()
        return bullet_images
