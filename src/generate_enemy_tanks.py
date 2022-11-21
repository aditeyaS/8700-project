import time, random
import const.app as AppConfig
import const.player as PlayerConfig
import const.enemy as EnemyConfig
from Tank import Tank

def generate_enemy_tanks(canvas):
    enemy_tanks = []
    for i in range(AppConfig.ENEMY_TANK_NUMBER):
        x = random.randint(0, AppConfig.WINDOW_WIDTH - EnemyConfig.ENEMY_TANK_WIDTH)
        y = random.randint(0, AppConfig.WINDOW_HEIGHT - EnemyConfig.ENEMY_TANK_WIDTH)
        d = random.choice(["up", "right", "down", "left"])
        c = random.choice(["red", "blue", "black"])
        enemy_tanks.append(Tank(x, y, d, c, canvas))
    return enemy_tanks