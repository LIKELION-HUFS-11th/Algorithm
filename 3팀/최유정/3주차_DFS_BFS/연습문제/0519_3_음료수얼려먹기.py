N, M = map(int, input().split())
ice_list = [list(map(int, input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(i, j):
    visited[i][j] = True
    for d in range(4):
        if i + dx[d] >= N or i + dx[d] < 0 or j + dy[d] >= M or j + dy[d] < 0:
            continue
        next_i = i + dx[d]
        next_j = j + dy[d]
        if ice_list[next_i][next_j] == 1 or visited[next_i][next_j] == True:
            visited[next_i][next_j] = True
            continue
        elif ice_list[next_i][next_j] == 0:
            dfs(next_i, next_j)
    return

for i in range(N):
    for j in range(M):
        if visited[i][j] == False and ice_list[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)