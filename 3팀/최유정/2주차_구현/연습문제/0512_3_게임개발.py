N, M = map(int, input().split())
A, B, d = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
total = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
map_list[A][B] = 2

while True:
    cnt = 0
    for i in range(4):
        d = (d-1) % 4
        if A + dx[d] >= M or A + dx[d] < 0 or B + dy[d] >= N or B + dy[d] < 0 or map_list[A+dx[d]][B+dy[d]] == 1 or map_list[A+dx[d]][B+dy[d]] == 2:
            cnt += 1
            continue
        else:
            A += dx[d]
            B += dy[d]
            total += 1
            map_list[A][B]=2
            break
    if cnt == 4:
        if map_list[A + dx[(d-2)%4]][B + dy[(d-2)%4]] == 1:
            break
        else:
            A += dx[(d-2)%4]
            B += dy[(d-2)%4]
print(total)