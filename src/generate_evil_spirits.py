import random
import const.app_config as AppConfig
import const.enemy as EnemyConfig
from GameObject import GameObject

def generate_evil_spirits(canvas):
    evil_spirits = []
    for i in range(AppConfig.ENEMY_TANK_NUMBER):
        x = random.randint(0, AppConfig.PLAYGROUND_WIDTH - EnemyConfig.ENEMY_TANK_WIDTH)
        y = random.randint(0, AppConfig.PLAYGROUND_HEIGHT - EnemyConfig.ENEMY_TANK_WIDTH)
        d = random.choice(["up", "right", "down", "left"])
        c = random.choice(["red", "blue", "black"])
        evil_spirits.append(GameObject(x, y, d, c, canvas))
    return evil_spirits