from tkinter import Frame, Entry, Canvas, PhotoImage, FLAT, W, E
import time

import const.app_config as AppConfig
import const.colors as Colors

from utils.delete_inactive import delete_inactive
from utils.collide import collide

from widgets.MainApp import MainApp
from widgets.PageFrame import PageFrame
from widgets.TitleLabel import TitleLabel
from widgets.CustomLabel import CustomLabel
from widgets.CustomFrame import CustomFrame
from widgets.CustomButtom import CustomButton

window = MainApp()

game_state = AppConfig.STORY

entered_username = ""

def on_start_click(username):
    global game_state
    game_state = AppConfig.PLAYGROUND
    global entered_username
    entered_username = username

def on_restart_click():
    global game_state
    game_state = AppConfig.STORY

def on_exit_click():
    global game_state
    game_state = AppConfig.EXIT


running = True

while running:
    if game_state == AppConfig.STORY:
        # frame for first page
        story_frame = PageFrame(window)

        game_title_label = TitleLabel(story_frame, AppConfig.GAME_NAME)

        description_frame = Frame(story_frame, padx=20, pady=20, bg="#000000")
        description_frame.grid(row=1, column=0)

        line_1_text = "It's haloween and the good spirits are coming down to"
        line1 = CustomLabel(description_frame, line_1_text)
        line1.grid(row=0, column=0)

        line_2_text = "give blessings to their loved ones. But the evil spirits"
        line2 = CustomLabel(description_frame, line_2_text)
        line2.grid(row=1, column=0)

        line_3_text = "are stopping their way."
        line3 = CustomLabel(description_frame, line_3_text)
        line3.grid(row=2, column=0)

        line_4_text = "Your mission is to destroy all the evil spirits"
        line4 = CustomLabel(description_frame, line_4_text)
        line4.grid(row=3, column=0)

        line_5_text = "Best of Luck!"
        line5 = CustomLabel(description_frame, line_5_text)
        line5.grid(row=4, column=0)

        username_input = Entry(story_frame, width=40, borderwidth=10, relief=FLAT)
        username_input.insert(0, "username")
        username_input.grid(row=2, column=0, padx=20, pady=20)

        start_button = CustomButton(story_frame, AppConfig.BTN_START, lambda: on_start_click(username_input.get()))
        start_button.grid(row=3, column=0, padx=20, pady=20)
        
        story_running = True
        while story_running == True:
            if (game_state != AppConfig.STORY):
                story_running = False                
            story_frame.update()
            time.sleep(0.1)

        if (story_running == False):
            story_frame.grid_forget()
            continue

    elif game_state == AppConfig.PLAYGROUND:
        pg_frame = PageFrame(window)
        pg_frame.grid_rowconfigure(1, weight=1)
        
        username_label = CustomLabel(pg_frame, entered_username, Colors.BABY_BLUE)
        username_label.grid(row=0, column=0)
        
        pg_canvas = Canvas(pg_frame, width=AppConfig.PLAYGROUND_WIDTH, height=AppConfig.PLAYGROUND_HEIGHT)
        pg_canvas.grid(row=1, column=0)
        bg_image = PhotoImage(file="../pic/bg.gif")
        pg_canvas.create_image(0, 0, image=bg_image, anchor="nw")

        status_row = Frame(pg_frame)
        status_row.grid(row=2, column=0)

        current_lives_text = f"Lives: {AppConfig.MAXIMUM_PLAYER_LIVES}/{AppConfig.MAXIMUM_PLAYER_LIVES}"
        lives_label = CustomLabel(status_row, current_lives_text, Colors.RED)
        lives_label.grid(row=0, column=0, sticky=W+E)

        score_label = CustomLabel(status_row, "Score: 0", Colors.GREEN)
        score_label.grid(row=0, column=1, sticky=W+E)
        
        from generate_evil_spirits import generate_evil_spirits
        from GameObject import GameObject

        evil_spirits = generate_evil_spirits(pg_canvas)
        evil_spirit_bullets = []

        # Pumpkin object and bullet
        pumpkin = GameObject(10, 10, "down", "huge", pg_canvas)
        pumpkin_bullets = []
        def shoot(event):
            pumpkin_bullets.append(pumpkin.create_bullet())

        # Bind keys with respond functions
        pg_canvas.bind_all('<Up>', pumpkin.set_dir_up)
        pg_canvas.bind_all('<Right>', pumpkin.set_dir_right)
        pg_canvas.bind_all('<Down>', pumpkin.set_dir_down)
        pg_canvas.bind_all('<Left>', pumpkin.set_dir_left)
        pg_canvas.bind_all('<space>', shoot)

        def update_status (current_lives, current_score):
            current_lives_text = f"Lives: {current_lives}/{AppConfig.MAXIMUM_PLAYER_LIVES}"
            global lives_label
            lives_label.config(text=current_lives_text)

            current_score_text = f"Score: {current_score}"
            global score_label
            score_label.config(text=current_score_text)

        count = 0
        player_lives = AppConfig.MAXIMUM_PLAYER_LIVES
        score = 0

        pg_running = True

        while pg_running:
            # update position and images of pumpkin
            pumpkin.update_pos_img()

            # update position and images of evis spirits
            for t in evil_spirits:
                t.update_pos_img()
                if count % 20 == 0:
                    evil_spirit_bullets.append(t.create_bullet())

            # update position and images of enemy bullets
            for b in evil_spirit_bullets:
                b.update_state()
                b.update_pos()
                if collide(b.get_pos(), pumpkin.get_pos()):
                    b.state = AppConfig.INACTIVE
                    pumpkin.state = AppConfig.EXPLODE

            # update position and state of player's bullets
            for b in pumpkin_bullets:
                b.update_state()
                b.update_pos()
                for t in evil_spirits:
                    if collide(b.get_pos(), t.get_pos()):
                        b.state = AppConfig.INACTIVE
                        t.state = AppConfig.EXPLODE

            # delete bullets that are out of window (INACTIVE)
            evil_spirit_bullets = delete_inactive(evil_spirit_bullets, pg_canvas)
            pumpkin_bullets = delete_inactive(pumpkin_bullets, pg_canvas)
            
            # delete evil spirits that finished exploding (INACTIVE)
            evil_spirits = delete_inactive(evil_spirits, pg_canvas)

            # calculation of lives and score
            score = (AppConfig.ENEMY_TANK_NUMBER - len(evil_spirits))*10

            if pumpkin.state == AppConfig.INACTIVE:
                player_lives -= 1
                if player_lives > 0:
                    pumpkin.state = AppConfig.ACTIVE

            update_status(player_lives, score)

            # check player status
            if pumpkin.state == AppConfig.INACTIVE:
                game_state = AppConfig.LEADERBOARD
                pg_running = False

            if len(evil_spirits) == 0:
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
            pg_frame.grid_remove()
            continue
        
        pg_canvas.mainloop()
    
    elif (game_state == AppConfig.LEADERBOARD):
        # frame for third page
        leaderboard_frame = PageFrame(window)

        leader_board_title = TitleLabel(leaderboard_frame, "Leader Board")

        table_frame = CustomFrame(leaderboard_frame)
        table_frame.grid(row=1, column=0, sticky="nsew")
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_columnconfigure(1, weight=1)

        c00 = CustomLabel(table_frame, text="Username")
        c00.grid(row=0, column=0)
        c01 = CustomLabel(table_frame, text="High Score")
        c01.grid(row=0, column=1)

        c10 = CustomLabel(table_frame, text="aditeys")
        c10.grid(row=1, column=0)
        c11 = CustomLabel(table_frame, text="10")
        c11.grid(row=1, column=1)

        c20 = CustomLabel(table_frame, text="aditeys")
        c20.grid(row=2, column=0)
        c21 = CustomLabel(table_frame, text="10")
        c21.grid(row=2, column=1)

        c30 = CustomLabel(table_frame, text="aditeys")
        c30.grid(row=3, column=0)
        c31 = CustomLabel(table_frame, text="10")
        c31.grid(row=3, column=1)

        c40 = CustomLabel(table_frame, text="aditeys")
        c40.grid(row=4, column=0)
        c41 = CustomLabel(table_frame, text="10")
        c41.grid(row=4, column=1)

        c50 = CustomLabel(table_frame, text="aditeys")
        c50.grid(row=5, column=0)
        c51 = CustomLabel(table_frame, text="10")
        c51.grid(row=5, column=1)
        

        action_row = CustomFrame(leaderboard_frame)
        action_row.grid(row=2, column=0, padx=20, pady=20)


        restart_button = CustomButton(action_row, AppConfig.BTN_RESUME, command=on_restart_click)
        restart_button.grid(row=0, column=0, sticky=W)
        
        exit_button = CustomButton(action_row, AppConfig.BTN_EXIT, command=on_exit_click)
        exit_button.grid(row=0, column=1, sticky=E)
        
        l_runing = True
        while l_runing == True:
            if (game_state != AppConfig.LEADERBOARD):
                l_runing = False             
            time.sleep(0.1)
            leaderboard_frame.update()


        
        if (l_runing == False):
            leaderboard_frame.grid_forget()
            continue
    elif (game_state == AppConfig.EXIT):
        window.quit()
        window.destroy()

    window.update()
window.mainloop()