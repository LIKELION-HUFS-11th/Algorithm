## 다른 노드로 이동할 때, 
## 새로운 노드까지의 거리 = 현재까지의 최단거리(dist)+해당 간선의 가중치(weight)
## 이 거리가 현재까지의 최단거리보다 작을 경우, 최단 거리 업데이트
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
## 입력
v, e = map(int,input().split()) # 정점 개수, 간선 개수
start = int(input()) # 시작 지점
data = [[] for _ in range(v+1)] # 간선에 대한 정보 저장된 2차원 리스트
for _ in range(e):
    s, e, w = map(int,input().split())
    data[s].append((e,w))

distance = [INF]*(v+1)  # 최단 경로 저장하는 리스트

q = [] # 우선순위 큐 선언하고
def dijkstra(start):
    distance[start] = 0 # 시작 지점은 0
    heapq.heappush(q,(0,start)) # 큐에 시작노드를 삽입
    while q:
        dist, now_node = heapq.heappop(q) # 현재까지의 최단거리와 현재 노드 꺼내서
        for n_n, weight in data[now_node]: 
            cost = dist + weight #이동할 노드까지의 거리 = 현재까지 최단 + 해당 간선 가중치
            if cost < distance[n_n]: # 그 거리가 현재까지의 최단거리보다 작을 경우
                distance[n_n] = cost # 최단거리 업데이트하고
                heapq.heappush(q,(cost,n_n)) # 큐에 삽입 

dijkstra(start)
for i in distance[1:]:
    if i != INF:
        print(i)
    else:
        print("INF")

        

