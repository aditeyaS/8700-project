import random

import const.app as AppConfig
import const.enemy as EnemyConfig

def generate_enemy_tanks():
    random_enemy_tank_list = []
    for i in range(AppConfig.ENEMY_TANK_NUMBER):
        # random x & y coordinate
        x = random.randint(0, AppConfig.WINDOW_WIDTH - EnemyConfig.ENEMY_TANK_WIDTH)
        x = random.randint(0, AppConfig.WINDOW_HEIGHT - EnemyConfig.ENEMY_TANK_HEIGHT)

        # random direction
        d = random.choice(AppConfig.DIRECTIONS)

        # random color
        c = random.choice(["red", "blue", "black"])

        # random_enemy_tank_list.append(Tank(x, y, d, c))
    return random_enemy_tank_list
