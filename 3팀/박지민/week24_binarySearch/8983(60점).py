## 입력
m, n, l = tuple(map(int, input().split())) 
gun_place = list(map(int, input().split())) # 총쏘는 위치
animal_place = [ tuple(map(int, input().split())) for _ in range(n)]

cnt = 0
visited = [] #방문 리스트

# 잡을 수 있는 동물의 수 
def can_shoot():
    for animal in animal_place:
        ani_x, ani_y = animal
        for k in gun_place:
            global cnt 
            distance = abs(ani_x-k) + ani_y
            if distance <= l and (ani_x, ani_y) not in visited:
                cnt += 1
                visited.append((ani_x, ani_y))

can_shoot()

print(cnt)