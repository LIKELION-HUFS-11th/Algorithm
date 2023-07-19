# 변수 선언
n, k = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
    ]

sec, x, y = map(int, input().split())


from collections import deque
q = deque()

visited = [[False]*n for _ in range(n)]

virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            virus.append([arr[i][j], i, j])

virus.sort()

for v in virus:
    q.append(v)

def multiply(virus_num, x, y):
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            arr[nx][ny] = virus_num
            q.append([arr[nx][ny], nx, ny])


def bfs():
    time = 0

    while q:
        if time >= sec:
            break

        for _ in range(len(q)):
            virus_num, vx, vy = q.popleft()
            if not visited[vx][vy]:
                visited[vx][vy] = 1
                multiply(virus_num, vx, vy)
        time += 1



bfs()

print(arr[x-1][y-1])






