from collections import deque

T = int(input())

dx, dy = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        a, b = q.popleft()
        if a == ex and b == ey:
            print(chess[a][b])
            break
        for i in range(8):
            na, nb = a + dx[i], b + dy[i]
            if 0 <= na < l and 0 <= nb < l and chess[na][nb] == 0:
                chess[na][nb] = chess[a][b] + 1
                q.append([na, nb])

for _ in range(T):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    chess = [[0]*l for _ in range(l)]
    bfs(sx, sy)