import sys
from collections import deque

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
maxnum = max(map(max, arr))

def bfs(a, b, water, visited):
    q = deque()
    q.append((a, b))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] > water and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

for i in range(0, maxnum):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    
    for j in range(n):
        for k in range(n):
            if arr[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1
    
    ans = max(ans, cnt)
    

print(ans)
        