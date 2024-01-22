import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if field[ny][nx] == 1:
                field[ny][nx] = 0
                dfs(nx,ny)

input = sys.stdin.readline
t = int(input()) # 테스트케이스 개수

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    count = 0                

    # 배추 위치 표시
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    # 배추 그룹 수 세기
    for x in range(m):
        for y in range(n):
            if field[y][x] == 1:
                dfs(x,y)
                count += 1 # 주변 배추를 탐색했는데 더 이상 1이 존재하지 않으면 count+1
    print(count)

