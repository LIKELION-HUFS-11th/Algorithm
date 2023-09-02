# 상하좌우

N = int(input())
A = list(input().split())

# R, D, L, U
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = ["R", "D", "L", "U"]

start_x, start_y = 1, 1
for a in A:
    d = dir.index(a)
    if start_x + dx[d] > N or start_x + dx[d] <= 0 or start_y + dy[d] <= 0 or start_y + dy[d] > N:
        continue
    else:
        start_x += dx[d]
        start_y += dy[d]

print(start_x, start_y)