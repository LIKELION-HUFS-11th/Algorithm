# n, m, k, x 입력
n, m, k, x = map(int, input().split())

# connection
connection = [[] for _ in range(n+1)]

# 연결 요소 입력
for _ in range(m):
    a, b = map(int, input().split())
    connection[a].append(b)

# bfs
def bfs():
    while q:
        curr_city = q.popleft()
        for next_city in connection[curr_city]:
            if not visited[next_city]:
                visited[next_city] = visited[curr_city] + 1
                q.append(next_city)

# visited
visited = [0 for _ in range(n+1)]

from collections import deque
q = deque()

visited[x] = 1
q.append(x)
bfs()

ans = []
for i in range(1, n+1):
    if visited[i] == k+1:
        ans.append(i)

if not ans:
    print(-1)
else:
    for a in ans:
        print(a)