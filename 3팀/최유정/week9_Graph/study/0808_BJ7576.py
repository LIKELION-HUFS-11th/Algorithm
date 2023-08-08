from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

check = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            check.append([i, j])

if len(check) == (n*m):
    print(0)
    exit(0)

while check:
    x, y = check.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            check.append([nx, ny])

result = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, tomato[i][j])

print(result-1)