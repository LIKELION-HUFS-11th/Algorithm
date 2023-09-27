tower_count = int(input(""))
tower_list = input("").split()

laser = []

i = tower_count-1
while i >= 0:
    tower_copy = tower_list[:i]

    if len(tower_copy) == 0:
        laser.append(0)
        break

    if len(tower_copy) == 1:
        if int(tower_copy[-1]) > int(tower_list[i]):
            laser.append(tower_list.index(tower_copy.pop())+1)
            i -= 1
            continue
        else:
            laser.append(0)
            i -= 1
            continue

    while int(tower_copy[-1]) < int(tower_list[i]) and len(tower_copy) > 2:
        tower_copy.pop()
    if len(tower_copy) == 2:
        if int(tower_copy[-1]) > int(tower_list[i]):
            laser.append(tower_list.index(tower_copy.pop())+1)
        else:
            laser.append(0)

    else:
        laser.append(tower_list.index(tower_copy.pop())+1)
    i -= 1

laser.reverse()
print(laser)
