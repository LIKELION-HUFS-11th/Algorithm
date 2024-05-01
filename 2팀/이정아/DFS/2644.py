import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
visited = [False] * (n+1)
result = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    visited[node] = True
    for near in graph[node]:
        if not visited[near]:
            result[near] = result[node] + 1
            dfs(near)

dfs(a)

if result[b] > 0:
    print(result[b])
else:
    print(-1)