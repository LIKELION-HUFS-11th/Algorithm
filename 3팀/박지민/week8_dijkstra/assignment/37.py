import heapq

# 도시 개수 n
n = int(input()) #5

# 버스 개수 m
m = int(input()) #14


# 버스 정보
graph = [ [] for _ in range(n+1) ]

for i in range(m):
    a,b,c = tuple(map(int, input().split()))
    # [도착지점, 비용]
    graph[a].append([b,c])

# 최단거리 리스트 초기화
distance = [int(1e9)] * (n+1)

#다익스트라
#heapq를 돌면서 distance 리스트를 업뎃
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start)) #(거리, 도착 노드) #0 = 같은 노드끼리의 거리, start
    distance[start] = 0

    while q:
        # 우선순위 큐에서 최소값인 (cost,city) pop
        #cost = 현재까지 찾은 시작도시~city 까지의 최단거리
        cost, city = heapq.heapop(q)

        # cost 보다 작을 경우
        if distance[city] < cost:
            continue
        # 현재 도시 city와 연결된 다른 도시들을 순회
        for node in graph[city]:
            #cost+ 도착비용(c)보다 클 경우
            if distance[node[0]] > cost+node[1]:
                distance[node[0]] = cost+node[1]
                heapq.heappush(q, (cost+node[1], node[0])) 
        
        

# 최소 비용 자료구조 
# min_cost = [
#     [0]
#     for _ in range(n)
# ]

# 버스 정보 : 시작 지점, 도착 지점, 비용
for _ in range(m):
    start, end, cost = tuple(map(int, input().split()))
    for i in range(n+1):
        for j in range(n+1):
            # 완전히 동일한 지점에 대한 최솟값
            if min_cost[i][j] > cost:
                min_cost[i][j] = cost
            
            # 1-> 4, 2-> 4
            # 거쳐가는 지점이 있는지 확인하고
            # 거쳐가는 지점들과 비교해서 최소인지

            if 
    


# 최단 거리 어떻게 함?

# 최소 비용
# [i][j] 

# 1-> 5 : 10 듦
# 1-> 2 : 2
# 2 -> 4 : 2
# 4 -> 5 :3     7 
# 1 -> 2


if 
min_cost[i][j] = min()

# 나만의 어떤 자료구조를 만들고 싶은데?
# min_cost = 2차원 배열 자료구조
# 최소 비용 자료구조를 만든다
  # 0 1 2 3 4 5
# 0   
# 1     2 3 1 10
# 2         2
# 3         1  1  
# 4            3
# 5 
 