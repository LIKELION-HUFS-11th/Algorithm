import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
arr = []
cbVisited, visited = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
for _ in range(n):
    arr.append(list(input().rstrip()))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
cbCnt, cnt = 0, 0

def cbBfs(x, y):
    global cbCnt
    cbCnt += 1
    q = deque()
    q.append((x, y))
    cbVisited[x][y] = 1
    now = [arr[x][y]]
    if now[0] == "R" or now[0] == "G":
        now = ["R", "G"]
    
    while q:
        a, b = q.popleft()
        for k in range(4):
            xx, yy = a+dx[k], b+dy[k]
            if 0 <= xx < n and 0 <= yy < n and not cbVisited[xx][yy] and arr[xx][yy] in now:
                q.append((xx, yy))
                cbVisited[xx][yy] = 1
        
def bfs(x, y):
    global cnt
    cnt += 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    now = arr[x][y]
    
    while q:
        a, b = q.popleft()
        for k in range(4):
            xx, yy = a+dx[k], b+dy[k]
            if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy] and arr[xx][yy] == now:
                q.append((xx, yy))
                visited[xx][yy] = 1

for i in range(n):
    for j in range(n):
        if not cbVisited[i][j]:
            cbBfs(i, j)
        if not visited[i][j]:
            bfs(i, j)

print(cnt, cbCnt)