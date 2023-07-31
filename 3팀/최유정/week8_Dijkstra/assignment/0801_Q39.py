from heapq import heappop, heappush
t = int(input())
INF = int(1e9)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(x, y):
    h = []
    heappush(h, (place[x][y], x, y))

    while h:
        dist, x, y = heappop(h)
        if visited[x][y] == 1: continue
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny <0 or nx >= n or ny >= n: continue
            check = dist + place[nx][ny]
            if check < graph[nx][ny]:
                graph[nx][ny] = check
                heappush(h, (check, nx, ny))


for _ in range(t):
    n = int(input())

    place = [list(map(int, input().split())) for _ in range(n)]
    graph = [[INF]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    graph[0][0] = place[0][0]
    solution(0, 0)
    print(graph[n-1][n-1])