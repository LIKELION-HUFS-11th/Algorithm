import sys, heapq, collections
n = int(input()) #정점 개수
m = int(input()) #간선 개수

graph = collections.defaultdict(list)
dist = collections.defaultdict(int) #방문 여부 저장

# for _ in range(n):
#     x, y, z = map(int, sys.stdin.readline().split())

# x, y = map(int, sys.stdin.readline().split())

for _ in range(m):
    depart, arrive, cost = map(int, sys.stdin.readline().split())
    graph[depart].append((cost, arrive)) #출발지가 키, 도착지와 비용이 value

start, end = map(int, sys.stdin.readline().split())

Q = [[0, start]] #우선순위 큐 초기화

while Q:
    cost, node = heapq.heappop(Q)
    if node not in dist: 
        dist[node] = cost #출발지랑 비용 저장
        
        for w, v in graph[node]: #graph의 해당 출발지랑 연결된 도착지와 비용들 돌기
            temp = cost + w
            heapq.heappush(Q, [temp, v])

print(dist[end])