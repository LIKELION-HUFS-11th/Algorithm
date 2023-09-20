tower_count = int(input(""))
tower_list = input("").split()

laser = []

i = tower_count-1
while i >= 0:
    tower_copy = tower_list[:i]
    count = 1

    if i != 0:
        received_tower = tower_copy[-1]
        while int(tower_copy[-1]) < int(tower_list[i]) and len(tower_copy) != 1:
            received_tower = tower_copy.pop()
            count += 1

        if len(tower_copy):
            laser.append(0)
        else:
            laser.append(tower_list.index(received_tower)+1)
    else:
        laser.append(0)
    i -= 1

laser.reverse()
print(laser)
