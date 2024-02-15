import sys
from collections import deque

def bfs(a, b):
    q = deque()
    q.append((a, b))
    arr = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and t_map[nx][ny] == "L" and not visited[nx][ny]:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
                visited[nx][ny] = True
        if arr[nx][ny] == n+m-2:
            break
        
    return max(map(max, arr))
                

def measure():
    ans = 0
    global n, m, t_map, dx, dy
    n, m = map(int, input().split())
    t_map = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(n):
        for j in range(m):
            if t_map[i][j] == "L":
                ans = max(ans, bfs(i, j))

    return ans

print(measure())