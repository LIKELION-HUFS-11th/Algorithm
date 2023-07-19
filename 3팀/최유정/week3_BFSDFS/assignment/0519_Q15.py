# 특정 거리의 도시 찾기

import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())

road = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    road[a].append(b)

visited = [False] * (N+1)

def bfs(x):
    visited[x] = True
    q = deque([(x, 0)])
    result = []
    while q:
        start, cnt = q.popleft()
        if cnt == K:
            result.append(start)
        for i in road[start]:
            if visited[i] == False:
                visited[i] = True
                q.append((i, cnt+1))
    return result

result = bfs(X)
result.sort()
if result == []:
    print(-1)
else:
    for i in result: print(i)