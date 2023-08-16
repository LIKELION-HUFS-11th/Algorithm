from collections import deque

N = int(input())
map_list = [list(input()) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    while check:
        x, y = check.popleft()
        color = map_list[x][y]
        if color == "G": map_list[x][y] = "R"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and map_list[nx][ny] == color:
                visited[nx][ny] = 1
                check.append([nx, ny])

answer = []
for _ in range(2):
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            check = deque()
            if visited[i][j] == 0:
                check.append([i, j])
                visited[i][j] = 1
                bfs()
                cnt += 1
    answer.append(cnt)

print(answer[0], answer[1])