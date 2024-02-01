import sys
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, broke):
    q.append((x, y, broke))
    
    while q:
        a, b, c = q.popleft()
        
        if a == n-1 and b == m-1:
            return visited[a][b][c]
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 벽 부수지 않고 이동
                if arr[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    q.append((nx, ny, c))
                    visited[nx][ny][c] = visited[a][b][c] + 1
                # 벽 부수고 이동
                if arr[nx][ny] == 1 and c == 0:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[a][b][c] + 1
    return -1

print(bfs(0, 0, 0))
    
