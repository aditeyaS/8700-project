import const.app as AppConfig

class TankImages:
    def getBlue(self):
        tank = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "tank_blue_" + d + ".gif"
            tank[d] = fileName
        return tank

    def getBlack(self):
        tank = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "tank_black_" + d + ".gif"
            tank[d] = fileName
        return tank

    def getRed(self):
        tank = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "tank_red_" + d + ".gif"
            tank[d] = fileName
        return tank

    def getPlayer(self):
        tank = {}
        for d in AppConfig.DIRECTIONS:
            fileName = "tank_player_" + d + ".gif"
            tank[d] = fileName
        return tank

    def getAll(self):
        tank_images = {}
        tank_images["blue"] = self.getBlue()
        tank_images["black"] = self.getBlack()
        tank_images["red"] = self.getRed()
        tank_images["player"] = self.getPlayer()
        return tank_images
