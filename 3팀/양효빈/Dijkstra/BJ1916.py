### 최소비용 구하기

# 단방향 그래프

# input
n = int(input())
m = int(input())

graph = { i : {} for i in range(1, n+1)}

# 같은 경로 존재할 때 최솟값으로 저장
for i in range(m):
    start, end, pay = map(int, input().split())
    if end in graph[start].keys():
        graph[start][end] = min(pay, graph[start][end])
    else: graph[start][end] = pay

start, end = map(int, input().split())


# 다익스트라

import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


ans = dijkstra(graph, start)

print(ans[end])