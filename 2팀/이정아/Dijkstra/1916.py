import sys
import heapq

# 두 노드 간의 최소비용 구하기 + 음수 간선 없음 + 가중치 존재 => 다익스트라

input = sys.stdin.readline
INF = int(1e9)

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    dep, arr, cost = map(int, input().split())
    # 버스의 graph[출발지].append([도착지, 비용])
    graph[dep].append([arr, cost])

start, end = map(int, input().split())
# 비용(거리) 초기값 무한대로 설정
distances = [INF] * (n+1)

def dijkstra(st):
    # 시작 노드까지의 거리 0
    distances[st] = 0
    q = []
    # 시작 노드부터 탐색 시작
    # 거리가 짧은 것들부터 방문해야 하므로 거리를 0번째 원소로
    heapq.heappush(q, (distances[st], st))
    
    while q:
        # 탐색할 노드, 출발지~해당 노드까지의 거리
        dist, node = heapq.heappop(q)
        # 현재 해당 노드의 최단거리가 탐색할 노드까지의 거리보다 짧다면 무시
        if distances[node] < dist:
            continue
        
        # 탐색할 노드와 연결된 인접노드들 탐색
        for n, d in graph[node]:
            # 출발지~인접노드까지의 거리
            distance = dist + d
            # 인접노드까지의 거리가 현재 해당 인접노드의 최단거리보다 짧다면
            if distance < distances[n]:
                # 현재 해당 인접노드의 최단거리 갱신 후 큐에 삽입
                distances[n] = distance
                heapq.heappush(q, (distance, n))

dijkstra(start)
# 도착 도시의 최단거리 출력
print(distances[end])