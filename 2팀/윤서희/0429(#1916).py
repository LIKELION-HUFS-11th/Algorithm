from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수
INF = 1e9  

buses = [[] for _ in range(n + 1)]  # 버스 정보 저장 리스트 
dp = [INF for _ in range(n + 1)]  # 각 도시에 도착하는 최소비용 리스트 (초기에는 무한값 넣기)

for i in range(m):
    a, b, c = list(map(int, input().split()))  # 출발도시, 도착도시, 비용
    buses[a].append((b, c))  # 출발도시 인덱스에 도착도시와 비용 저장

start, end = map(int, input().split())  # 목표시작점, 목표끝점

# 다익스트라
def dijkstra(x):
    dp[x] = 0  # 시작점이므로 0의 비용으로 도착

    heap = []
    heappush(heap, [0, x]) # 비용과 현재 좌표 리스트로 힙에 값 넣기

    while heap:
        cost, point = heappop(heap) # 비용, 현재 좌표
        if dp[point] < cost: # dp 리스트의 현재 좌표까지 오는 비용이 지금까지 비용보다 적다면
            continue # 넘어감

        for fin, money in buses[point]: #현재 좌쵸에서 출발하는 경로 순회
            new_cost = cost + money # 비용 더하기

            if dp[fin] > new_cost: # 지금까지 든 비용보다 작다면
                dp[fin] = new_cost # 값 갱신
                heappush(heap, [new_cost, fin]) # 새로운 비용과 현재 좌표 힙에 넣기

dijkstra(start)
print(dp[end]) # dp 리스트의 도착지까지 가는 비용 출력