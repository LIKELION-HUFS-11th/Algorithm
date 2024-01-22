# 1. 현재 칸이 청소되지 않았다면 -> 청소
# 2. 현재 칸의 상하좌우를 검사하는데
# -> 청소되지 않은 빈칸이 없다면
# 현재 방향에서 후진 가능하면 : 한 칸 후진 후 현재 칸의 청소여부 검사 (즉 1번으로 돌아감)
# 현재 방향에서 후진 불가하면: 거기서 작동 끝
# -> 청소되지 않은 빈칸이 있다면
# -> 반시계방향으로 90도 회전하고 
# --> 그 바라보는 방향 기준으로 앞쪽이 청소되지 않은 빈 칸이라면 -> 한 칸 전진하고 그 칸의 청소여부 검사 (즉 1번으로 돌아감)

# 북동남서
# 0123

# 그래프의 값이 0이면 -> 청소 안 된 곳, 1이면-> 벽

# 입력 및 변수 선언
n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# dx, dy
#  북동남서
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 함수
def cleaner(x, y ,dir):
    global cnt
    cnt = 0
    if graph[x][y] == 0:
        graph[x][y] = 2 # 청소한다
        cnt += 1
    # 상하좌우를 검사하는데
    # 현재 남쪽을 바라본다면 동으로 가야
    for i in range(4):
        nx = x + dx[(dir+3)%4] 
        ny = y + dy[(dir+3)%4]
        if graph[nx][ny] == 0:
            return cleaner(nx, ny, ((dir+3)%4))
    # 현재 남쪽을 바라본다면 북으로 가야
    # (dir+2)%4
    # 
    back_x = x + dx[(dir+2)%4]
    back_y = y + dy[(dir+2)%4]
    if graph[back_x][back_y] != 1:
        return cleaner(back_x, back_y, dir)
    
    return cnt

print(cleaner(r, c, d))