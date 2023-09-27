from collections import deque

dx, dy = [0, 1, 0, -1, -1, 1, 1, -1], [1, 0, -1, 0, 1, 1, -1, -1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    while q:
        a, b = q.popleft()
        for i in range(8):
            na, nb = a + dx[i], b + dy[i]
            if 0 <= na < h and 0 <= nb < w and map_list[na][nb] == 1 and visited[na][nb] == False:
                q.append([na, nb])
                visited[na][nb] = True

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    map_list = []
    visited = [[False]*w for _ in range(h)]
    result = 0
    for _ in range(h):
        map_list.append(list(map(int, input().split())))
    for x in range(h):
        for y in range(w):
            if map_list[x][y] == 1 and visited[x][y] == False:
                bfs(x, y)
                result += 1
    print(result)