import sys
input = sys.stdin.readline

def change_lights(lights):
    for elem in lights.keys():
        info = lights[elem]
        how_long = info[2][1] #현재 신호등의 지속시간

        if info[2][0] == "r":
            limit = info[0] #현재 신호등 시간 리밋
            next = "g" #다음으로 바뀌어야 하는 색깔
        else:
            limit = info[1]
            next = "r"

        if how_long == limit: #불이 바뀌어야 함
            lights[elem][2] = [next, 1]
        else:
            lights[elem][2][1] += 1 #else : 현재 신호등 지속시간 + 1

    return




n, l = map(int, input().split())

road = [0 for _ in range(l+1)] #도로 시작은 0, 끝은 l
lights = dict()

for _ in range(n):
    d, r, g = map(int, input().split())

    road[d] = 1
    lights[d] = [r, g, ["r", 0]] #key:신호등위치 / value:빨간불시간, 초록불시간, [현재상태, 몇초째현재상태인지]


time, i = 0, 0
while i < l:
    if road[i] == 0:
        i += 1

    else: #현재 위치에 신호등 있음
        color = lights[i][2][0] #현재 신호등의 색깔 : 초록색이면 1 전진, 아니면 제자리
        if color == "g":
            i += 1


    if i == l:
        break

    time += 1
    change_lights(lights)



#i = l 도착
print(time)