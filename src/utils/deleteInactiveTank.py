import const.app as AppConfig

def delete_inactive_tanks(tank_list, canvas):
    new_tank_list = []
    for tank in tank_list:
        if tank.state == AppConfig.INACTIVE:
            canvas.delete(tank.drawable)
            del tank
        else:
            new_tank_list.append(tank)
    return new_tank_list