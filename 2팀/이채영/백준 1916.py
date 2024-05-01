# import sys
# input = sys.stdin.readline

# n = int(input().strip())
# m = int(input().strip())

# cities = [[0 for _ in range(n+1)] for _ in range(n+1)]
# """
# a/s 0   1   2   ... n
# 0
# 1
# 2
# ...
# n
# """

# for _ in range(m):
#     s, a, c = map(int, input().split())
#     cities[s][a] = c ##s->a 비용 c 

# start, arrive = map(int, input().split())

import sys
import heapq 

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
        
start, end = map(int, input().split())
costs = [1e9 for _ in range(n+1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])
    
while heap:
    cur_cost, cur_v = heapq.heappop(heap)
    if costs[cur_v] < cur_cost:
        continue
    for next_v, next_cost in graph[cur_v]:
        sum_cost = cur_cost + next_cost
        if sum_cost >= costs[next_v]:
            continue
        
        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])
        
print(costs[end])