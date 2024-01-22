import heapq

## 입력
dangers = []
N = int(input())
for _ in range(N):
   map(int, input().split())

M = int(input())

# 안전한 구역은 0, 위험한 곳은 1, 죽음의 구역은 2로 
graph = [[0] * 501 for _ in range(501)]

distance = [[float("inf")] * 501 for _ in range(501)]
start = 0
distance[start] = 0

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist[now]:
            continue
        # 인접 노드
        if graph[i][j] == 1:
            if distance (dist[now] + 1)


