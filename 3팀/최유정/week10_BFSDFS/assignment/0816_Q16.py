# https://www.acmicpc.net/problem/14502
from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
lab = [list(map(int, input().split(" "))) for _ in range(N)]
virus = []
able = []
cnt = 0
result = 0

for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append([i, j])
        elif lab[i][j] == 0:
            able.append([i, j])
            cnt += 1

virus = deque(virus)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

able_list = combinations(able, 3)

def bfs(lab, cnt):
    new_virus = deepcopy(virus)
    while new_virus:
        x, y = new_virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                new_virus.append([nx, ny])
                cnt -= 1
    return cnt

for al in able_list:
    new_lab = deepcopy(lab)
    for x, y in al:
        new_lab[x][y] = 1
    result = max(result, bfs(new_lab, cnt-3))

print(result)