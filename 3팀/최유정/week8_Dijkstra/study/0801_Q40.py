# 숨바꼭질 : 가장 큰 값 구하기
# 헛간 번호, 거리, 같은 거리를 갖는 헛간의 개수

from heapq import heappop, heappush

INF = int(1e9)
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
check = [INF] * n
visited = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

h = []
heappush(h, (0, 1))
visited[0] = 1
check[0] = 0

while h:
    dist, now = heappop(h)
    visited[now-1] = 1
    for i in graph[now]:
        if visited[i-1] != 1:
            cost = dist + 1
            if cost < check[i-1]:
                check[i-1] = cost
                heappush(h, (cost, i))

print(check)

max_street = max(check)
cnt = check.count(max_street)
min_num = 0
for i in range(n):
    if check[i] == max_street:
        min_num = i+1
        break

print(min_num, max_street, cnt)