from tkinter import Label, Frame, Entry, Canvas, PhotoImage, FLAT, W, E
import time

import const.app_config as AppConfig
import const.colors as Colors

from utils.delete_inactive import delete_inactive
from utils.collide import collide

from db.LeaderboardDB import LeaderboardDB

from widgets.MainApp import MainApp
from widgets.PageFrame import PageFrame
from widgets.CustomFrame import CustomFrame
from widgets.CustomButtom import CustomButton
from widgets.LabelFactory import LabelFactory

window = MainApp()
leaderboard_db = LeaderboardDB()
label_factory = LabelFactory()

game_state = AppConfig.STORY

def on_start_click():
    global game_state
    game_state = AppConfig.PLAYGROUND

def on_restart_click():
    global game_state
    game_state = AppConfig.STORY

def on_exit_click():
    global game_state
    game_state = AppConfig.EXIT


running = True
did_player_win = False

while running:
    if game_state == AppConfig.STORY:
        # frame for first page
        story_frame = PageFrame(window)

        game_title_label = label_factory.getLabel(AppConfig.LABEL_TITLE, story_frame, AppConfig.GAME_NAME)

        description_frame = Frame(story_frame, padx=20, pady=20, bg="#000000")
        description_frame.grid(row=1, column=0)

        line_1_text = "Oh NO! Evil Spirits have risen from the cemetery and"
        label_factory.getLabel(AppConfig.LABEL_NORMAL, description_frame, line_1_text).grid(row=0, column=0)

        line_2_text = "invaded Clemson! You are our only hope! Cleanse the area"
        label_factory.getLabel(AppConfig.LABEL_NORMAL, description_frame, line_2_text).grid(row=1, column=0)

        line_3_text = "with the help of your powerful pumpkin!"
        label_factory.getLabel(AppConfig.LABEL_NORMAL, description_frame, line_3_text).grid(row=2, column=0)

        line_4_text = "The world's fate depends on you now!"
        label_factory.getLabel(AppConfig.LABEL_NORMAL, description_frame, line_4_text).grid(row=3, column=0)

        line_5_text = "Best of Luck!"
        label_factory.getLabel(AppConfig.LABEL_NORMAL, description_frame, line_5_text).grid(row=4, column=0)

        username_input = Entry(story_frame, width=40, borderwidth=10, relief=FLAT)
        username_input.insert(0, "username")
        username_input.grid(row=2, column=0, padx=20, pady=20)

        start_button = CustomButton(story_frame, AppConfig.BTN_START, command=on_start_click)
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
        # frame for second page
        pg_frame = PageFrame(window)
        pg_frame.grid_rowconfigure(1, weight=1)
        
        label_factory.getLabel(AppConfig.LABEL_NORMAL,pg_frame, username_input.get(), Colors.BABY_BLUE).grid(row=0, column=0)
        
        pg_canvas = Canvas(pg_frame, width=AppConfig.PLAYGROUND_WIDTH, height=AppConfig.PLAYGROUND_HEIGHT)
        pg_canvas.grid(row=1, column=0)
        bg_image = PhotoImage(file="../pic/bg.gif")
        pg_canvas.create_image(0, 0, image=bg_image, anchor="nw")

        status_row = Frame(pg_frame)
        status_row.grid(row=2, column=0)

        current_lives_text = f"Lives: {AppConfig.MAXIMUM_PLAYER_LIVES}/{AppConfig.MAXIMUM_PLAYER_LIVES}"
        lives_label = label_factory.getLabel(AppConfig.LABEL_NORMAL,status_row, current_lives_text, Colors.RED)
        lives_label.grid(row=0, column=0, sticky=W+E)

        score_label = label_factory.getLabel(AppConfig.LABEL_NORMAL,status_row, "Score: 0", Colors.GREEN)
        score_label.grid(row=0, column=1, sticky=W+E)
        
        from generate_evil_spirits import generate_evil_spirits
        from GameObject import GameObject

        evil_spirits = generate_evil_spirits(pg_canvas)
        evil_spirit_bullets = []

        # Pumpkin object and bullet
        pumpkin = GameObject(10, 10, "down", "pumpkin", pg_canvas)
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
            score = (AppConfig.EVIL_SPIRIT_NUMBER - len(evil_spirits))*10

            if pumpkin.state == AppConfig.INACTIVE:
                player_lives -= 1
                if player_lives > 0:
                    pumpkin.state = AppConfig.ACTIVE

            update_status(player_lives, score)

            # check player status
            if pumpkin.state == AppConfig.INACTIVE:
                did_player_win = False
                leaderboard_db.write_score(username_input.get().strip(), score)
                game_state = AppConfig.LEADERBOARD
                pg_running = False

            if len(evil_spirits) == 0:
                did_player_win = True
                leaderboard_db.write_score(username_input.get().strip(), score)
                game_state = AppConfig.LEADERBOARD
                pg_running = False

            count += 1
            pg_canvas.update()
            time.sleep(0.1)

        if (pg_running == False):
            continue
        
        pg_canvas.mainloop()
    
    elif (game_state == AppConfig.LEADERBOARD):
        # frame for third page
        leaderboard_top_5 = leaderboard_db.read_score()
        leaderboard_frame = PageFrame(window)

        label_factory.getLabel(AppConfig.LABEL_TITLE, leaderboard_frame, "Leader Board")
        
        if did_player_win:
            status_text = "You WIN!!"
            status_color = Colors.GREEN
        else:
            status_text = "You LOOSE!!"
            status_color = Colors.RED

        Label(
            leaderboard_frame,
            text=status_text,
            font='Arial 16',
            background=Colors.BLACK,
            foreground=status_color
        ).grid(row=1, column=0, sticky="nswe")

        table_frame = CustomFrame(leaderboard_frame)
        table_frame.grid(row=2, column=0, sticky="nsew")
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_columnconfigure(1, weight=1)

        label_factory.getLabel(AppConfig.LABEL_NORMAL, table_frame, text="Username").grid(row=0, column=0)
        label_factory.getLabel(AppConfig.LABEL_NORMAL, table_frame, text="High Score").grid(row=0, column=1)

        for _row in range(5):
            for _col in range(2):
                label_factory.getLabel(AppConfig.LABEL_NORMAL, table_frame, text=leaderboard_top_5[_row][_col]).grid(row=1+_row, column=_col)

        action_row = CustomFrame(leaderboard_frame)
        action_row.grid(row=3, column=0, padx=20, pady=20)

        CustomButton(
            action_row,
            AppConfig.BTN_RESUME,
            command=on_restart_click
        ).grid(row=0, column=0, sticky=W)
        
        CustomButton(
            action_row,
            AppConfig.BTN_EXIT,
            command=on_exit_click
        ).grid(row=0, column=1, sticky=E)
        
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