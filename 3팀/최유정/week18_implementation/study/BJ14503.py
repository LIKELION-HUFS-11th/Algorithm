# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
# 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
# 3-1. 반시계 방향으로 90도 회전한다.
# 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 3-3. 1번으로 돌아간다.
# 북동남서
# 현재 자리가 청소가 되어 있지 않으면 청소
# 90도씩 돌면서 청소가 되어 있는지 확인
# 안 되어 있다면 전진
# 되어 있다면 그 상태에서 후진하기
# 현재 남이고 동으로 가야함
# d+1 = 4
# 4+i = 7, 6, 5, 4
# n = 2, 1, 0, 3 (d = 3) 1
# n = 1, 0, 3, 2 (d = 2) 2
# n = 0, 3, 2, 1 (d = 1) 3
# n = 3, 2, 1, 0 (d = 0) 4
# -d + 4



N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def room_service(x, y, dir):
    global cnt
    if room[x][y] == 0:
        room[x][y] = -1
        cnt += 1
    for i in range(3, -1, -1):
        nx = x + dx[(i+dir)%4]
        ny = y + dy[(i+dir)%4]
        if room[nx][ny] == 0:
            return room_service(nx, ny, ((i+dir)%4))
    back_x = x + dx[(dir+2)%4]
    back_y = y + dy[(dir+2)%4]
    if room[back_x][back_y] != 1:
        return room_service(back_x, back_y, dir)
    return cnt

print(room_service(r, c, d))