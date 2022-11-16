from tkinter import *
import time, random

import const.app as AppConfig
import const.enemy as EnemyConfig
import const.player as PlayerConfig

from init.ExplosionImages import ExplosionImages
from init.TankImages import TankImages
from init.BulletImages import BulletImages

win = Tk()
# win.attributes('-fullscreen', True)

can = Canvas(win, width=AppConfig.WINDOW_WIDTH, height=AppConfig.WINDOW_HEIGHT)
can.pack(expand = True)

# import background pictures
bg = PhotoImage(file="../pic/bg.gif")
can.create_image(0, 0, image=bg, anchor="nw")

# A dictionart to store tanks' images
tanks_img = TankImages().getAll()

# images of exploring tank
explosion = ExplosionImages().getExplosionImages()

# bullet_images = BulletImages
bullets_img = BulletImages().getAll()

class Tank():

    def __init__(self, x, y, d, c):
        
        self.color = c
        self.dir = d
        self.speed = 5
        self.drawable = can.create_image(x, y,
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
            can.itemconfig(self.drawable, image=explosion[self.e_count])
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

            can.itemconfig(self.drawable, image=tanks_img[self.color][self.dir])

            # change tank's position
            if self.dir == "up":
                can.move(self.drawable, 0, -self.speed)
            elif self.dir == "left":
                can.move(self.drawable, -self.speed, 0)
            elif self.dir == "down":
                can.move(self.drawable, 0, self.speed)
            elif self.dir == "right":
                can.move(self.drawable, self.speed, 0)

    def create_bullet(self):
        if self.color == "huge":
            b_w = PlayerConfig.PLAYER_BULLET_WIDTH
            b_h = PlayerConfig.PLAYER_BULLET_HEIGHT

        else:
            b_w = EnemyConfig.ENEMY_BULLET_WIDTH
            b_h = EnemyConfig.ENEMY_BULLET_HEIGHT

        # To calculate the initial position of a bullet
        b_pos = self.get_pos()
        if self.dir == "up":
            b_pos = [b_pos[0] + (self.width-b_w)/2, b_pos[1]]
        elif self.dir == "down":
            b_pos = [b_pos[0] + (self.width-b_w)/2, b_pos[1] + self.height]
        elif self.dir == "left":
            b_pos = [b_pos[0], b_pos[1] + (self.height-b_w)/2]
        elif self.dir == "right":
            b_pos = [b_pos[0] + self.width, b_pos[1] + (self.height - b_w)/2]

        b = Bullet(b_pos, self.color, self.dir, b_w)
        return b


    def get_pos(self):
        b_pos = can.coords(self.drawable)
        b_pos = b_pos + [b_pos[0] + self.width, b_pos[1] + self.height]
        return b_pos


    def set_dir_up(self, event):
        self.dir = "up"


    def set_dir_down(self, event):
        self.dir = "down"

    def set_dir_left(self, event):
        self.dir = "left"

    def set_dir_right(self, event):
        self.dir = "right"


class Bullet():
    def __init__(self, pos, c, d, w):
        self.color = c
        self.width = w
        self.dir = d
        self.imgs = bullets_img[self.color]
        self.speed = AppConfig.BULLET_SPEED
        self.drawable = can.create_image(pos[0], pos[1], image=self.imgs[self.dir], anchor="nw")
        self.state = AppConfig.ACTIVE

    def update_pos(self):
        can.itemconfig(self.drawable, image=self.imgs[self.dir])
        if self.dir == "up":
            can.move(self.drawable, 0, -self.speed)
        elif self.dir == "left":
            can.move(self.drawable, -self.speed, 0)
        elif self.dir == "down":
            can.move(self.drawable, 0, self.speed)
        elif self.dir == "right":
            can.move(self.drawable, self.speed, 0)

    def update_state(self):
        b_pos = self.get_pos()

        if b_pos[0] < 0 or b_pos[1] < 0 or b_pos[2] > AppConfig.WINDOW_WIDTH or b_pos[3] > AppConfig.WINDOW_HEIGHT:
            self.state = AppConfig.INACTIVE

    def get_pos(self):
        b_pos = can.coords(self.drawable)
        b_pos = b_pos + [b_pos[0] + self.width, b_pos[1] + self.width]
        return b_pos


# MAIN PROGRAM
# Tank and bullet list for enemies' tanks
enemy_tanks = []
enemy_bullets = []

for i in range(AppConfig.ENEMY_TANK_NUMBER):
    x = random.randint(0, AppConfig.WINDOW_WIDTH - EnemyConfig.ENEMY_TANK_WIDTH)
    y = random.randint(0, AppConfig.WINDOW_HEIGHT - EnemyConfig.ENEMY_TANK_WIDTH)
    d = random.choice(["up", "left", "down", "right"])
    c = random.choice(["red", "blue", "black"])
    enemy_tanks.append(Tank(x, y, d, c))

# Tank and bullet list for player's tanks
player_tank = Tank(10, 10, "down", "huge")
player_bullets = []


def shoot(event):
    player_bullets.append(player_tank.create_bullet())


# Bind keys with respond functions
can.bind_all('<Up>', player_tank.set_dir_up)
can.bind_all('<Left>', player_tank.set_dir_left)
can.bind_all('<Down>', player_tank.set_dir_down)
can.bind_all('<Right>', player_tank.set_dir_right)
can.bind_all('<space>', shoot)


def is_collide(a, b):
    if a[0] < b[2] and a[1] < b[3] and a[2] > b[0] and a[3] > b[1]:
        return True
    else:
        return False


def delete_useless(obj_list):
    new_obj_list = []
    for obj in obj_list:
        if obj.state == AppConfig.INACTIVE:
            can.delete(obj.drawable)
            del obj
        else:
            new_obj_list.append(obj)
    return new_obj_list


count = 0
player_lives = AppConfig.MAXIMUM_PLAYER_LIVES
score = 0
lives_text = can.create_text(10, 10, anchor='nw', text='lives: '+str(player_lives),
                       font=('Consolas', 15))

score_text = can.create_text(150, 10, anchor='nw', text='score: '+str(score),
                       font=('Consolas', 15))

running = True

while running:
    # Update position and images of player's tank
    player_tank.update_pos_img()

    # Update position and images of enemies' tanks
    for t in enemy_tanks:
        t.update_pos_img()
        if count % 20 == 0:
            enemy_bullets.append(t.create_bullet())

    # Update position and images of enemies' bullets
    for b in enemy_bullets:
        b.update_state()
        b.update_pos()
        if is_collide(b.get_pos(), player_tank.get_pos()):
            b.state = AppConfig.INACTIVE
            player_tank.state = AppConfig.EXPLODE

    # Update position and state of player's bullets
    for b in player_bullets:
        b.update_state()
        b.update_pos()
        for t in enemy_tanks:
            if is_collide(b.get_pos(), t.get_pos()):
                b.state = AppConfig.INACTIVE
                t.state = AppConfig.EXPLODE

    # Delete useless bullets that are out of window.
    # Delete Tanks that finished exploding.
    enemy_bullets = delete_useless(enemy_bullets)
    enemy_tanks = delete_useless(enemy_tanks)
    player_bullets = delete_useless(player_bullets)

    # Calculation of hp and score
    score = (AppConfig.ENEMY_TANK_NUMBER - len(enemy_tanks))*10

    if player_tank.state == AppConfig.INACTIVE:
        player_lives -= 1
        if player_lives > 0:
            player_tank.state = AppConfig.ACTIVE

    can.itemconfig(lives_text, text='lives: '+str(player_lives))
    can.itemconfig(score_text, text='score: '+str(score))

    # Game is end or not
    if player_tank.state == AppConfig.INACTIVE:
        can.create_text(AppConfig.WINDOW_WIDTH/2, AppConfig.WINDOW_HEIGHT/2,
                    text='YOU LOSE!nscore:'+str(score),
                    font=('Lithos Pro Regular', 30))
        running = False

    if len(enemy_tanks) == 0:
        can.create_text(AppConfig.WINDOW_WIDTH / 2, AppConfig.WINDOW_HEIGHT / 2,
                        text='YOU WIN! score:' + str(score),
                        font=('Lithos Pro Regular', 30))
        running = False

    count += 1
    can.update()
    time.sleep(0.1)

can.mainloop()