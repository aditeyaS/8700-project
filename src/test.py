from tkinter import *
import time

import const.app as AppConfig

from utils.delete_inactive import delete_inactive
from utils.collide import collide

window = Tk()
window.title("Haloween Hunter")
window.geometry("800x800")
window.resizable(False, False)

running = True
game_state = AppConfig.STORY

def on_start_click():
    global game_state
    game_state = AppConfig.PLAYGROUND

def on_restart_click():
    global game_state
    game_state = AppConfig.STORY

def on_exit_click():
    window.quit()

while running:
    print(game_state)
    if game_state == AppConfig.STORY:
        story_frame = Frame(window, height=800, width=800, bg="#000000")
        story_frame.pack(expand=True, fill=BOTH)
        story_frame.pack_propagate(0)

        

        print(story_frame.winfo_height)

        welcome_label = Label(story_frame, anchor=CENTER, text="Haloween Hunter", background="#000000", foreground="#ffffff")
        welcome_label.grid(row=1, sticky=E+W, columnspan=1)

        textAbout = "Welcome to Haloween unter.\n Here you have to duuwduwdu"
        welcome_label = Label(story_frame, anchor=CENTER, text=textAbout, background="#000000", foreground="#ffffff")
        welcome_label.grid(row=2)
        
        hibernation_mode = Label(story_frame, anchor=CENTER, text="Hibernation Mode", background="#000000", foreground="#ffffff")
        hibernation_mode.grid(row=3)

        # story_canvas = Canvas(window, width=AppConfig.WINDOW_WIDTH, height=AppConfig.WINDOW_HEIGHT)
        start_button = Button(story_frame, text="Start", command=on_start_click)

        # story_canvas.grid(row=1, column=0)
        start_button.grid(row=4)
        
        story_running = True
        while story_running == True:
            if (game_state != AppConfig.STORY):
                story_running = False                
            story_frame.update()
            time.sleep(0.1)

        if (story_running == False):
            story_frame.pack_forget()
            # start_button.grid_forget()
            continue
        # story_frame.mainloop()

    elif game_state == AppConfig.PLAYGROUND:
        frame = Frame(window, width=800, height=800)
        frame.place(x=0, y=0)
        pg_canvas = Canvas(frame, width=AppConfig.WINDOW_WIDTH, height=AppConfig.WINDOW_HEIGHT)
        pg_canvas.grid(row=1, column=0, columnspan=2)
        bg_image = PhotoImage(file="../pic/bg.gif")
        pg_canvas.create_image(0, 0, image=bg_image, anchor="nw")

        from generate_enemy_tanks import generate_enemy_tanks
        from Tank import Tank

        enemy_tanks = generate_enemy_tanks(pg_canvas)
        enemy_bullets = []

        # Tank and bullet list for player's tanks
        player_tank = Tank(10, 10, "down", "huge", pg_canvas)
        player_bullets = []
        def shoot(event):
            player_bullets.append(player_tank.create_bullet())

        # Bind keys with respond functions
        pg_canvas.bind_all('<Up>', player_tank.set_dir_up)
        pg_canvas.bind_all('<Right>', player_tank.set_dir_right)
        pg_canvas.bind_all('<Down>', player_tank.set_dir_down)
        pg_canvas.bind_all('<Left>', player_tank.set_dir_left)
        pg_canvas.bind_all('<space>', shoot)
        
        username_label = Label(frame, text="aditeys", bd=1, relief=SUNKEN, pady=5)
        username_label.grid(row=0, column=0, sticky=W+E, columnspan=2)

        current_lives_text = "Lives: " + str(AppConfig.MAXIMUM_PLAYER_LIVES) + "/" + str(AppConfig.MAXIMUM_PLAYER_LIVES)
        lives_label = Label(frame, text=current_lives_text, relief=SUNKEN, anchor=W)
        lives_label.grid(row=2, column=0, sticky=W+E)

        score_label = Label(frame, text="Score: " + str(0), relief=SUNKEN, anchor=E)
        score_label.grid(row=2, column=1, sticky=W+E)
        
        def update_status (current_lives, current_score):
            current_lives_text = "Lives: " + str(current_lives) + "/" + str(AppConfig.MAXIMUM_PLAYER_LIVES)
            global lives_label
            lives_label = Label(frame, text=current_lives_text, relief=SUNKEN, anchor=W)
            lives_label.grid(row=2, column=0, sticky=W+E)

            global score_label
            score_label = Label(frame, text="Score: " + str(current_score), relief=SUNKEN, anchor=E)
            score_label.grid(row=2, column=1, sticky=W+E)

        # update_status(AppConfig.MAXIMUM_PLAYER_LIVES, 0)

        count = 0
        player_lives = AppConfig.MAXIMUM_PLAYER_LIVES
        score = 0
        # lives_text = canvas.create_text(10, 10, anchor='nw', text='lives: '+str(player_lives),
                            #    font=('Consolas', 15))

        # score_text = canvas.create_text(150, 10, anchor='nw', text='score: '+str(score),
                            #    font=('Consolas', 15))

        pg_running = True

        while pg_running:
            # update position and images of player's tank
            player_tank.update_pos_img()

            # update position and images of enemy tanks
            for t in enemy_tanks:
                t.update_pos_img()
                if count % 20 == 0:
                    enemy_bullets.append(t.create_bullet())

            # update position and images of enemy bullets
            for b in enemy_bullets:
                b.update_state()
                b.update_pos()
                if collide(b.get_pos(), player_tank.get_pos()):
                    b.state = AppConfig.INACTIVE
                    player_tank.state = AppConfig.EXPLODE

            # update position and state of player's bullets
            for b in player_bullets:
                b.update_state()
                b.update_pos()
                for t in enemy_tanks:
                    if collide(b.get_pos(), t.get_pos()):
                        b.state = AppConfig.INACTIVE
                        t.state = AppConfig.EXPLODE

            # delete bullets that are out of window (INACTIVE)
            enemy_bullets = delete_inactive(enemy_bullets, pg_canvas)
            player_bullets = delete_inactive(player_bullets, pg_canvas)
            
            # delete tanks that finished exploding (INACTIVE)
            enemy_tanks = delete_inactive(enemy_tanks, pg_canvas)

            # calculation of lives and score
            score = (AppConfig.ENEMY_TANK_NUMBER - len(enemy_tanks))*10

            if player_tank.state == AppConfig.INACTIVE:
                player_lives -= 1
                if player_lives > 0:
                    player_tank.state = AppConfig.ACTIVE

            # canvas.itemconfig(lives_text, text='lives: '+str(player_lives))
            # canvas.itemconfig(score_text, text='score: '+str(score))
            update_status(player_lives, score)

            # check player status
            if player_tank.state == AppConfig.INACTIVE:
                # canvas.create_text(AppConfig.WINDOW_WIDTH/2, AppConfig.WINDOW_HEIGHT/2,
                #             text='YOU LOSE!nscore:'+str(score),
                #             font=('Lithos Pro Regular', 30))
                game_state = AppConfig.LEADERBOARD
                pg_running = False

            if len(enemy_tanks) == 0:
                # canvas.create_text(AppConfig.WINDOW_WIDTH / 2, AppConfig.WINDOW_HEIGHT / 2,
                #                 text='YOU WIN! score:' + str(score),
                #                 font=('Lithos Pro Regular', 30))
                game_state = AppConfig.LEADERBOARD
                pg_running = False

            count += 1
            pg_canvas.update()
            time.sleep(0.1)

        if (pg_running == False):
            score_label.grid_forget()
            username_label.grid_forget()
            score_label.grid_forget()
            lives_label.grid_forget()
            pg_canvas.grid_forget()
            frame.grid_remove()
            continue
        
        pg_canvas.mainloop()
    elif (game_state == AppConfig.LEADERBOARD):
        leaderboard_frame = Frame(window, height=800, width=800, bg="red")
        leaderboard_frame.pack()
        leaderboard_frame.pack_propagate(0)
    
        # leaderboard_canvas = Canvas(window, width=AppConfig.WINDOW_WIDTH, height=AppConfig.WINDOW_HEIGHT)
        # leaderboard_canvas.grid(row=1, column=0, columnspan=2)

        restart_button = Button(leaderboard_frame, text="Restart", command=on_restart_click)
        restart_button.grid(row=1, column=1)
        
        exit_button = Button(leaderboard_frame, text="Exit", command=window)
        exit_button.grid(row=1, column=2)
        
        l_runing = True
        while l_runing == True:
            if (game_state != AppConfig.LEADERBOARD):
                l_runing = False                
            time.sleep(0.1)
            leaderboard_frame.update()

        if (l_runing == False):
            # print("HERE " + game_state)
            leaderboard_frame.pack_forget()
            # restart_button.grid_remove()
            # exit_button.grid_remove()
            continue
        # leaderboard_frame.mainloop()

    window.update()
window.mainloop()