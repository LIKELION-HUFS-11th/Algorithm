import sys
input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())

'''
f: 총 층 수
g: 스타트링크의 위치
s: 지금 위치
u: 위로
d: 아래로
'''
graph = [0] * (f + 1)
visited = [0] * (f + 1)

def bfs(s):
    q = deque([s])
    visited[s] = 1

    while q:
        n = q.popleft()

        if n == g:
            return graph[n]
        
        for i in [n + u, n - d]:
            if 0 < i <= f and visited[i] == 0:
                visited[i] = 1
                graph[i] = graph[n] + 1
                q.append(i)

    return "use the stairs"
    
print(bfs(s))