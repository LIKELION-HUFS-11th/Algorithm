import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 정의
def dfs(x, y):
    dx = [0, 0, -1, 1] 
    dy = [1, -1, 0, 0]

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안에 있고 1이면(=배추이면) 지나간것을 -1로 표시하고 주변 탐색
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx, ny)

t = int(input()) 
for _ in range(t):
    m, n, k = map(int, input().split()) 
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        X, Y = map(int, input().split()) 
        graph[Y][X] = 1 

    count = 0
    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                dfs(a ,b)
                count += 1
    print(count)