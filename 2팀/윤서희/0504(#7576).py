import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())   # 가로 / 세로
tomato = []
for _ in range(n):
    a = list(map(int, input().split()))
    tomato.append(a)

''' tomato
[[0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1]]
'''

good = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            good.append((i, j, 0))

''' good
[[3, 5, 1]]
'''
cnt = 0
while good:
    x, y, a = good.popleft()
    if x - 1 >= 0:
        if tomato[x - 1][y] == 0:
            good.append((x - 1, y, a + 1))
            tomato[x - 1][y] = 1
            cnt = a + 1
    if x + 1 < n:
        if tomato[x + 1][y] == 0:
            good.append((x + 1, y, a + 1))
            tomato[x + 1][y] = 1
            cnt = a + 1
    if y - 1 >= 0:
        if tomato[x][y - 1] == 0:
            good.append((x, y - 1, a + 1))
            tomato[x][y - 1] = 1
            cnt = a + 1
    if y + 1 < m:
        if tomato[x][y + 1] == 0:
            good.append((x, y + 1, a + 1))
            tomato[x][y + 1] = 1
            cnt = a + 1


''' tomato
[[1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1, 1]]
'''

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            cnt = -1
            
    
print(cnt)
        