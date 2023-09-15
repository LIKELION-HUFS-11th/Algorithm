### 최단경로


# 정점 수, 간선 수
vertics, edge = map(int, input().split())

# 시작 정점
start = int(input())

# 그래프 생성
graph = { i:{} for i in range(1, vertics+1)}

for i in range(edge):
    u, v, w = map(int, input().split())
    if v in graph[u].keys():
        graph[u][v] = min(w, graph[u][v])
    else: graph[u][v] = w  # 주의: 방향그래프이므로 한 방향으로만 저장


import heapq

def dijkstra(graph, start):
    # 시작 노드로부터의 최단 거리를 저장하는 딕셔너리
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 우선순위 큐를 사용하여 탐색할 노드와 거리를 저장
    priority_queue = [(0, start)]

    while priority_queue:
        # 현재 노드와 현재까지의 최단 거리를 가져옴
        current_distance, current_node = heapq.heappop(priority_queue)

        # 현재까지의 거리가 이미 더 작은 경우 스킵
        if current_distance > distances[current_node]:
            continue

        # 현재 노드의 인접 노드를 순회
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 더 짧은 거리를 발견한 경우 업데이트하고 우선순위 큐에 추가
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


ans = dijkstra(graph, start)

for i in range(1, vertics+1):
    if ans[i] == float('inf'):
        print('INF')
    else: print(ans[i])



# keypoint: 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.