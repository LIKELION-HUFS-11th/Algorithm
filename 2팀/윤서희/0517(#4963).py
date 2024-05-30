import sys
input = sys.stdin.readline
from collections import deque


def bfs(maps, x, y, w, h):
    land = deque()
    land.append((x, y))
    maps[x][y] = 0

    while land:
        x, y = land.popleft()
        
        # 위
        if x - 1 >= 0:
            if maps[x - 1][y] == 1:
                land.append((x - 1, y))
                maps[x - 1][y] = 0
        # 아래
        if x + 1 < h:
            if maps[x + 1][y] == 1:
                land.append((x + 1, y))
                maps[x + 1][y] = 0
        # 왼쪽
        if y - 1 >= 0:
            if maps[x][y - 1] == 1:
                land.append((x, y - 1))
                maps[x][y - 1] = 0
        # 오른쪽
        if y + 1 < w:
            if maps[x][y + 1] == 1:
                land.append((x, y + 1))
                maps[x][y + 1] = 0
        # 왼쪽 아래
        if x - 1 >= 0 and y - 1 >= 0:
            if maps[x - 1][y - 1] == 1:
                land.append((x - 1, y - 1))
                maps[x - 1][y - 1] = 0
        # 오른쪽 아래
        if x - 1 >= 0 and y + 1 < w:
            if maps[x - 1][y + 1] == 1:
                land.append((x - 1, y + 1))
                maps[x - 1][y + 1] = 0
        # 오른쪽 위
        if x + 1 < h and y + 1 < w:
            if maps[x + 1][y + 1] == 1:
                land.append((x + 1, y + 1))
                maps[x + 1][y + 1] = 0
        # 왼쪽 위
        if x + 1 < h and y - 1 >= 0:
            if maps[x + 1][y - 1] == 1:
                land.append((x + 1, y - 1))
                maps[x + 1][y - 1] = 0
    return cnt
                



while True:
    w, h = map(int, input().split()) # 지도의 너비 w, 높이 h
    
    # 입력 종료 조건
    if w == 0 and h == 0:
        break

    maps = []  # 지도
    cnt = 0  # 섬의 개수
    for _ in range(h):
        width = list(map(int, input().split()))
        maps.append(width)
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                bfs(maps, i, j, w, h)
                cnt += 1
    
    print(cnt)
