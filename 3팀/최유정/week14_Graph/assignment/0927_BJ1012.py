from collections import deque

T = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(a, b):
    q = deque()
    q.append([a, b])
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if visited[nx][ny] == False and map_list[nx][ny] == 1:
                q.append([nx,ny])
                visited[nx][ny] = True

for _ in range(T):
    M, N, K = map(int, input().split())
    result = 0
    map_list = [[0] * M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    b = deque()
    for _ in range(K):
        y, x = map(int, input().split())
        map_list[x][y] = 1
        b.append([x, y])
    while b:
        x, y = b.popleft()
        if visited[x][y] == False:
            bfs(x, y)
            result += 1
    print(result)