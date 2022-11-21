import const.app as AppConfig

def delete_inactive(object_list, canvas):
    new_object_list = []
    for object in object_list:
        if object.state == AppConfig.INACTIVE:
            canvas.delete(object.drawable)
            del object
        else:
            new_object_list.append(object)
    return new_object_list