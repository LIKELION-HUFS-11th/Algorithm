import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    dx, dy = [0, 0, 1, -1, 1, -1, 1, -1], [1, -1, 1, -1, -1, 1, 0, 0]
    arr[x][y] = 0
    
    q = deque()
    q.append((x, y))
    
    while q:
        a, b = q.popleft()
        for i in range(8):
            xx, yy = a+dx[i], b+dy[i]
            if 0<=xx<h and 0<=yy<w and arr[xx][yy] == 1:
                q.append((xx, yy))
                arr[xx][yy] = 0
        
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    ans = 0
    arr = []
    for i in range(h):
        arr.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i, j)
                ans += 1
    print(ans)
                        