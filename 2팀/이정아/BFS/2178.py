from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, list(input()))))
dx, dy = [-1,1,0,0], [0,0,1,-1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            xxx, yyy = xx+dx[i], yy+dy[i]
            # 지도 범위 안이고, 아직 방문하지 않았다면 다음에 방문하도록 큐에 추가
            if 0 <= xxx < n and 0 <= yyy < m and maze[xxx][yyy] == 1:
                maze[xxx][yyy] = maze[xx][yy] + 1
                q.append((xxx, yyy))

bfs(0, 0)
print(maze[n-1][m-1])