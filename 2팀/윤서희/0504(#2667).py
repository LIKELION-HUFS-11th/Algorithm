import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
house = []
for _ in range(n):
    a = list(map(int, input().strip())) 
    house.append(a)

'''
[[0, 1, 1, 0, 1, 0, 0], 
 [0, 1, 1, 0, 1, 0, 1], 
 [1, 1, 1, 0, 1, 0, 1], 
 [0, 0, 0, 0, 1, 1, 1], 
 [0, 1, 0, 0, 0, 0, 0], 
 [0, 1, 1, 1, 1, 1, 0], 
 [0, 1, 1, 1, 0, 0, 0]]
'''

def bfs(house, x, y):
    danji = deque()
    n = len(house)
    danji.append((x, y))
    house[x][y] = 0
    cnt = 1

    while danji:
        x, y = danji.popleft()
        if x - 1 >= 0:
            if house[x - 1][y] == 1:
                danji.append((x - 1, y))
                house[x - 1][y] = 0
                cnt += 1
        if x + 1 < n:
            if house[x + 1][y] == 1:
                danji.append((x + 1, y))
                house[x + 1][y] = 0
                cnt += 1
        if y - 1 >= 0:
            if house[x][y - 1] == 1:
                danji.append((x, y - 1))
                house[x][y - 1] = 0
                cnt += 1
        if y + 1 < n:
            if house[x][y + 1] == 1:
                danji.append((x, y + 1))
                house[x][y + 1] = 0
                cnt += 1
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            ans.append(bfs(house, i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)