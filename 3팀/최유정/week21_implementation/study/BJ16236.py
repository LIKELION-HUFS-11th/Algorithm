from heapq import heappop, heappush

N = int(input())
fish = [list(map(int, input().split())) for _ in range(N)]
cur_x, cur_y = 0, 0
cur_fish = 2
cnt = 0
dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_shortest_route(i, j):
    h = []
    heappush(h, (0, i, j))
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    check, cx, cy = float('inf'), 100, 100
    while h:
        c, x, y = heappop(h)
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and fish[nx][ny] <= cur_fish:
                visited[nx][ny] = c + 1
                if visited[nx][ny] > check:
                    return cx, cy, check
                if 1 <= fish[nx][ny] < cur_fish:
                    if nx < cx or (nx == cx and ny < cy): check, cx, cy = visited[nx][ny], nx, ny
                    else: continue
                heappush(h, (visited[nx][ny], nx, ny))
    return cx, cy, check


for i in range(N):
    for j in range(N):
        if fish[i][j] == 9:
            cur_x, cur_y = i, j
        if fish[i][j] > 0 and fish[i][j] < 2:
            cnt += 1

if cnt == 0:
    print(0)
else:
    eat = 0
    result = 0
    while True:
        if eat == cur_fish:
            eat = 0
            cur_fish += 1
        fish[cur_x][cur_y] = 0
        cur_x, cur_y, r = find_shortest_route(cur_x, cur_y)
        if cur_x == 100:
            break
        result += r
        eat += 1

    print(result)