from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(m)]
graph = [[0]*n for _ in range(m)]
graph[0][0] = 1

check = deque()
check.append([0, 0])

while(check):
    x, y = check.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n:
            if graph[nx][ny] == 0:
                if miro[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] # 그냥 통과하기
                    check.appendleft([nx, ny])
                else:
                    graph[nx][ny] = graph[x][y]+1 # 부수기(후순위)
                    check.append([nx, ny])


print(graph[m-1][n-1]-1)