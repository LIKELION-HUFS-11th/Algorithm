# 왕실의 나이트

c = list(input())

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]
cnt = 0

start_x, start_y = alp.index(c[0])+1, int(c[1])

for i in range(8):
    if start_x + dx[i] <= 0 or start_x + dx[i] > 8 or start_y + dy[i] <= 0 or start_y + dy[i] > 8:
        continue
    else:
        cnt += 1

print(cnt)