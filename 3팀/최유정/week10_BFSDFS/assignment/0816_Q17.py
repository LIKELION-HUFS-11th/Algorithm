# https://www.acmicpc.net/problem/18405
from collections import deque

N, K = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def find(map_list):
    virus = []
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == 0: continue
            virus.append([map_list[i][j], i, j])
    virus.sort()
    return deque(virus)


def bfs(map_list):
    virus = find(map_list)
    cnt = 0

    while cnt < S:
        for _ in range(len(virus)):
            num, vx, vy = virus.popleft()

            for i in range(4):
                nx, ny = vx + dx[i], vy + dy[i]
                if nx >= N or nx < 0 or ny >= N or ny < 0 or map_list[nx][ny]!=0: continue

                map_list[nx][ny] = num
                virus.append([num, nx, ny])
        cnt += 1
    return map_list[X-1][Y-1]

print(bfs(map_list))