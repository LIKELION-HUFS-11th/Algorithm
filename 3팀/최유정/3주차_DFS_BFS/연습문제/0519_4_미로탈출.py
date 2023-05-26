from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        a, b = q.popleft()
        for i in range(4):
            if a + dx[i] >= N or a + dx[i] < 0 or b + dy[i] >= M or b + dy[i] < 0:
                continue
            next_a, next_b = a + dx[i], b + dy[i]
            if maze[next_a][next_b] == 1:
                maze[next_a][next_b] += maze[a][b]
                q.append((next_a, next_b))
    return maze[N-1][M-1]

print(bfs(0, 0))
