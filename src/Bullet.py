import const.app as AppConfig

from init.BulletImages import BulletImages

bullets_img = BulletImages().getAll()

class Bullet():
    def __init__(self, position, color, direction, width, can):
        global canvas
        canvas = can
        self.color = color
        self.width = width
        self.dir = direction
        self.imgs = bullets_img[self.color]
        self.speed = AppConfig.BULLET_SPEED
        self.drawable = canvas.create_image(position[0], position[1], image=self.imgs[self.dir], anchor="nw")
        self.state = AppConfig.ACTIVE

    def update_pos(self):
        canvas.itemconfig(self.drawable, image=self.imgs[self.dir])
        if self.dir == "up":
            canvas.move(self.drawable, 0, -self.speed)
        elif self.dir == "right":
            canvas.move(self.drawable, self.speed, 0)
        elif self.dir == "down":
            canvas.move(self.drawable, 0, self.speed)
        elif self.dir == "left":
            canvas.move(self.drawable, -self.speed, 0)

    def update_state(self):
        bullet_pos = self.get_pos()
        if bullet_pos[0] < 0 or bullet_pos[1] < 0 or bullet_pos[2] > AppConfig.WINDOW_WIDTH or bullet_pos[3] > AppConfig.WINDOW_HEIGHT:
            self.state = AppConfig.INACTIVE

    def get_pos(self):
        bullet_pos = canvas.coords(self.drawable)
        bullet_pos = bullet_pos + [bullet_pos[0] + self.width, bullet_pos[1] + self.width]
        return bullet_pos