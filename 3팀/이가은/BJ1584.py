import sys
sys.setrecursionlimit(10001)

grid = [[0] * 501 for _ in range(501)]
visited = [[False] * 501 for _ in range(501)]

def initialize(x1, y1, x2, y2, num):
    if x1 > x2:
        tmp = x1
        x1 = x2
        x2 = tmp
    if y1 > y2:
        tmp = y1
        y1 = y2
        y2 = tmp

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] = num

critical = int(input())
for _ in range(critical):
    cri_x1, cri_y1, cri_x2, cri_y2 = list(map(int, input().split()))
    initialize(cri_x1, cri_y1, cri_x2, cri_y2, 1)

death = int(input())
for _ in range(death):
    dth_x1, dth_y1, dth_x2, dth_y2 = list(map(int, input().split()))
    initialize(dth_x1, dth_y1, dth_x2, dth_y2, -1)

# for row in grid:
#     for elem in row:
#         print(elem, end=" ")
#     print()

# 오 아래 왼 위 
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
def in_range(x, y):
    return 0 <= x and x < 501 and 0 <= y and y < 501

life = 0
def dfs(x, y):
    global life
    visited[x][y] = True

    if x != 0 or y != 0:
        life += grid[x][y]
    
    if x == 500 and y == 500:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny):
            if not visited[nx][ny] and grid[nx][ny] != -1:
                dfs(nx, ny)

dfs(0, 0)
if not visited[500][500]:
    print(-1)
else:
    print(life)
