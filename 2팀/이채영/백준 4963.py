# 런타임

import sys
input = sys.stdin.readline

global maps

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def countIslands():
    global maps

    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                cnt += 1
                dfs(i, j)
    
    return cnt

def dfs(x, y):
    global maps

    maps[x][y] = 0

    satisfied = False

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx > h - 1 or ny > w - 1:
            continue
        else:
            if maps[nx][ny] == 1:
                satisfied = True
                dfs(nx, ny)

    if not satisfied: #더이상 갈 곳이 없으면
        return





result = []
while True:
    w, h = tuple(map(int, input().split()))
    
    if w == 0 and h == 0:
        break

    maps = []
    for _ in range(h):
        maps.append(list(map(int, input().split())))

    result.append(countIslands())

for elem in result:
    print(elem)