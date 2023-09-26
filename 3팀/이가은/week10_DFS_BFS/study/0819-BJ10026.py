import sys
sys.setrecursionlimit(10001)

n = int(input())

blind_data = [[0] * n for _ in range(n)]
data = [
    list(input())
    for _ in range(n)
]

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if data[i][j] == 'G' or data[i][j] == 'R':
            blind_data[i][j] = 1

def initialize(graph, n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = False

dxs = [1, -1, 0,  0]
dys = [0,  0, 1, -1]

def dfs(graph, x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if (not visited[nx][ny]) and graph[x][y] == graph[nx][ny]:
                dfs(graph, nx, ny)

cnt, blind_cnt = 0, 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(data, i, j)
            cnt += 1

initialize(visited, n)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(blind_data, i, j)
            blind_cnt += 1

print(cnt, blind_cnt)
