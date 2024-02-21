import sys
from collections import deque

n, m = map(int, input().split())
graph = [] #보물지도 정보

ans = 0

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 바다(W)는 이동 불가, 육지(L)로만 이동 가능
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

# BFS 로 최단 거리 탐색 
def bfs(x, y):
    global ans
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]

            if nx <0 or nx >= n or ny <0 or ny >= m:
                continue
            if graph[x][y] == "W":
                continue
            if graph[x][y] == "L" and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
                ans = max(distance[nx][ny], ans)
    return ans

for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            distance = [[-1] * m for _ in range(n)]
            distance[i][j] = 0
            bfs(i,j)

print(ans)