from collections import deque

N, M = map(int, input().split())
island = [list(input()) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j):
  visited = [[0]*M for _ in range(N)]
  q = deque()
  q.append((i, j))
  visited[i][j] = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and island[nx][ny] == 'L' and not visited[nx][ny]:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))
  return max(map(max, visited))

result=0
for i in range(N):
  for j in range(M):
    if island[i][j]=='L':
      result=max(result,bfs(i,j))

print(result-1)