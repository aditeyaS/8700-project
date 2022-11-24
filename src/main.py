from tkinter import *
import time

import const.app as AppConfig

from utils.delete_inactive import delete_inactive
from utils.collide import collide

window = Tk()
window.title("Haloween Hunter")

running = True

STORY = "STORY"
PLAYGROUND = "PLAYGROUND"

# game_state = STORY
# while running:
#     if game_state == STORY:
#         if (story_screen(window)):
#             game_state = PLAYGROUND
#     elif game_state == PLAYGROUND:
#         playground_screen(window)
#     print(game_state)
# window.mainloop()
# win.attributes('-fullscreen', True)

# canvas = Canvas(window, width=AppConfig.WINDOW_WIDTH, height=AppConfig.WINDOW_HEIGHT)
# # canvas.pack(expand = True)
# canvas.grid(row=1, column=0, columnspan=2)
# # canvas.forget()
# # import background pictures
# bg_image = PhotoImage(file="../pic/bg.gif")
# canvas.create_image(0, 0, image=bg_image, anchor="nw")

# from generate_enemy_tanks import generate_enemy_tanks
# from Tank import Tank

# enemy_tanks = generate_enemy_tanks(canvas)
# enemy_bullets = []

# # Tank and bullet list for player's tanks
# player_tank = Tank(10, 10, "down", "huge", canvas)
# player_bullets = []
# def shoot(event):
#     player_bullets.append(player_tank.create_bullet())

# # Bind keys with respond functions
# window.bind_all('<Up>', player_tank.set_dir_up)
# window.bind_all('<Right>', player_tank.set_dir_right)
# window.bind_all('<Down>', player_tank.set_dir_down)
# window.bind_all('<Left>', player_tank.set_dir_left)
# window.bind_all('<space>', shoot)

# username = Label(window, text="aditeys", bd=1, relief=SUNKEN, pady=5)
# username.grid(row=0, column=0, sticky=W+E, columnspan=2)

# def update_status (current_lives, current_score):
#     current_lives_text = "Lives: " + str(current_lives) + "/" + str(AppConfig.MAXIMUM_PLAYER_LIVES)
#     global lives
#     lives = Label(window, text=current_lives_text, bd=1, relief=SUNKEN, anchor=W)
#     lives.grid(row=2, column=0, sticky=W+E)

#     global score
#     score = Label(window, text="Score: " + str(current_score), bd=1, relief=SUNKEN, anchor=E)
#     score.grid(row=2, column=1, sticky=W+E)

# update_status(AppConfig.MAXIMUM_PLAYER_LIVES, 0)

# count = 0
# player_lives = AppConfig.MAXIMUM_PLAYER_LIVES
# score = 0
# # lives_text = canvas.create_text(10, 10, anchor='nw', text='lives: '+str(player_lives),
#                     #    font=('Consolas', 15))

# # score_text = canvas.create_text(150, 10, anchor='nw', text='score: '+str(score),
#                     #    font=('Consolas', 15))

# running = True

# while running:
#     # update position and images of player's tank
#     player_tank.update_pos_img()

#     # update position and images of enemy tanks
#     for t in enemy_tanks:
#         t.update_pos_img()
#         if count % 20 == 0:
#             enemy_bullets.append(t.create_bullet())

#     # update position and images of enemy bullets
#     for b in enemy_bullets:
#         b.update_state()
#         b.update_pos()
#         if collide(b.get_pos(), player_tank.get_pos()):
#             b.state = AppConfig.INACTIVE
#             player_tank.state = AppConfig.EXPLODE

#     # update position and state of player's bullets
#     for b in player_bullets:
#         b.update_state()
#         b.update_pos()
#         for t in enemy_tanks:
#             if collide(b.get_pos(), t.get_pos()):
#                 b.state = AppConfig.INACTIVE
#                 t.state = AppConfig.EXPLODE

#     # delete bullets that are out of window (INACTIVE)
#     enemy_bullets = delete_inactive(enemy_bullets, canvas)
#     player_bullets = delete_inactive(player_bullets, canvas)
    
#     # delete tanks that finished exploding (INACTIVE)
#     enemy_tanks = delete_inactive(enemy_tanks, canvas)

#     # calculation of lives and score
#     score = (AppConfig.ENEMY_TANK_NUMBER - len(enemy_tanks))*10

#     if player_tank.state == AppConfig.INACTIVE:
#         player_lives -= 1
#         if player_lives > 0:
#             player_tank.state = AppConfig.ACTIVE

#     # canvas.itemconfig(lives_text, text='lives: '+str(player_lives))
#     # canvas.itemconfig(score_text, text='score: '+str(score))
#     update_status(player_lives, score)

#     # check player status
#     if player_tank.state == AppConfig.INACTIVE:
#         canvas.create_text(AppConfig.WINDOW_WIDTH/2, AppConfig.WINDOW_HEIGHT/2,
#                     text='YOU LOSE!nscore:'+str(score),
#                     font=('Lithos Pro Regular', 30))
#         running = False

#     if len(enemy_tanks) == 0:
#         canvas.create_text(AppConfig.WINDOW_WIDTH / 2, AppConfig.WINDOW_HEIGHT / 2,
#                         text='YOU WIN! score:' + str(score),
#                         font=('Lithos Pro Regular', 30))
#         running = False

#     count += 1
#     canvas.update()
#     time.sleep(0.1)

# canvas.mainloop()