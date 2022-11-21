import random

import const.app as AppConfig
import const.player as PlayerConfig
import const.enemy as EnemyConfig

from init.TankImages import TankImages
from init.ExplosionImages import ExplosionImages

from Bullet import Bullet

# all the explosion images
explosion = ExplosionImages().getExplosionImages()

# all tank images
tanks_img = TankImages().getAll()

class Tank():

    def __init__(self, x, y, direction, color, can):
        # TODO: Add tank_type field (should not be based on color)
        global canvas
        canvas = can
        self.color = color
        self.dir = direction
        self.speed = 5
        self.drawable = canvas.create_image(x, y,
                                         image=tanks_img[self.color][self.dir],
                                         anchor="nw")
        self.state = AppConfig.ACTIVE
        self.e_count = 0
 
        if self.color == "huge":
            self.width = PlayerConfig.PLAYER_TANK_WIDTH
            self.height = PlayerConfig.PLAYER_TANK_HEIGHT
        else:
            self.width = EnemyConfig.ENEMY_TANK_WIDTH
            self.height = EnemyConfig.ENEMY_TANK_HEIGHT

    # Update the appearance and state of the tank
    def update_pos_img(self):
        if self.state == AppConfig.INACTIVE:
            pass

        elif self.state == AppConfig.EXPLODE:
            # change images
            canvas.itemconfig(self.drawable, image=explosion[self.e_count])
            self.e_count += 1
            # if it is the last one
            if self.e_count == 5:
                self.state = AppConfig.INACTIVE
                self.e_count = 0

        elif self.state == AppConfig.ACTIVE:
            t_pos = self.get_pos()

            # When touching wall, change direction arbitarily
            if t_pos[0] < 0:
                self.dir = random.choice(["down", "up", "right"])
            elif t_pos[1] < 0:
                self.dir = random.choice(["down", "left", "right"])
            elif t_pos[2] > AppConfig.WINDOW_WIDTH:
                self.dir = random.choice(["down", "up", "left"])
            elif t_pos[3] > AppConfig.WINDOW_HEIGHT:
                self.dir = random.choice(["left", "up", "right"])

            canvas.itemconfig(self.drawable, image=tanks_img[self.color][self.dir])

            # change tank's position
            if self.dir == "up":
                canvas.move(self.drawable, 0, -self.speed)
            elif self.dir == "right":
                canvas.move(self.drawable, self.speed, 0)
            elif self.dir == "down":
                canvas.move(self.drawable, 0, self.speed)
            elif self.dir == "left":
                canvas.move(self.drawable, -self.speed, 0)

    def create_bullet(self):
        if self.color == "huge":
            b_w = PlayerConfig.PLAYER_BULLET_WIDTH
            # b_h = PlayerConfig.PLAYER_BULLET_HEIGHT

        else:
            b_w = EnemyConfig.ENEMY_BULLET_WIDTH
            # b_h = EnemyConfig.ENEMY_BULLET_HEIGHT

        # calculate the initial position of a bullet
        b_pos = self.get_pos()
        if self.dir == "up":
            b_pos = [b_pos[0] + (self.width-b_w)/2, b_pos[1]]
        elif self.dir == "right":
            b_pos = [b_pos[0] + self.width, b_pos[1] + (self.height - b_w)/2]
        elif self.dir == "down":
            b_pos = [b_pos[0] + (self.width-b_w)/2, b_pos[1] + self.height]
        elif self.dir == "left":
            b_pos = [b_pos[0], b_pos[1] + (self.height-b_w)/2]
        b = Bullet(b_pos, self.color, self.dir, b_w, canvas)
        return b


    def get_pos(self):
        b_pos = canvas.coords(self.drawable)
        b_pos = b_pos + [b_pos[0] + self.width, b_pos[1] + self.height]
        return b_pos


    def set_dir_up(self, event):
        self.dir = "up"

    def set_dir_right(self, event):
        self.dir = "right"

    def set_dir_down(self, event):
        self.dir = "down"

    def set_dir_left(self, event):
        self.dir = "left"