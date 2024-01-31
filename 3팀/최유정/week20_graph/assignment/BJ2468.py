from collections import deque

n = int(input())
area = []
max_height = 0
for _ in range(n):
    a = list(map(int, input().split(" ")))
    max_height = max(max(a), max_height)
    area.append(a)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check_area(visited, n , rain, area, j, k):
    q = deque([])
    q.append([j, k])
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] > rain and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

result = 0
for i in range(max_height):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if area[j][k] > i and not visited[j][k]:
                check_area(visited, n, i, area, j, k)
                cnt += 1
    result = max(result, cnt)

print(result)