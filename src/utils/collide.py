def collide(a, b):
    if a[0] < b[2] and a[1] < b[3] and a[2] > b[0] and a[3] > b[1]:
        return True
    else:
        return False