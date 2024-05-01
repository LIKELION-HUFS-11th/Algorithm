import sys
from itertools import combinations

n, m =map(int, sys.stdin.readline().split())

chicken = [] #치킨집들 좌표
home = []   #집들 좌표

for i in range(n): #따로 저장
    nList = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if nList[j] == 1:
            home.append((i,j))
        elif nList[j] == 2:
            chicken.append((i,j))

# for i in range(n):
#     oneList = list(map(int, sys.stdin.readline().split()))
#     nList.append(oneList)
# nList = nList[1:]

# nResult = [[0]*n]*n #각 집의 치킨거리 기재.-> for문 돌면서 치킨거리 총합 구하기

def cal_dist(x,y):  #거리 구하기
    return abs(x[0]-y[0]) +abs(x[1] - y[1])

result = float('inf')
for x in combinations(chicken, m):
    # 치킨집 좌표 리스트 요소들의 M개 조합 돌기
  graph_dist = 0
  for h in home: # 전체 집 순회
    home_dist = float('inf')
    
    for k in x: # 각 집별로 치킨집 순회
      home_dist = min(home_dist, cal_dist(h, k)) # 집별로 가장 가까운 치킨집 거리
    graph_dist += home_dist # 도시 치킨 거리 += 집에서 가장 가까운 치킨집 거리
  result = min(result, graph_dist)

print(result)


# def chicken(n, m, home, chicken):
#     ans = float('inf')
#     dists =[] #치킨집으로부터 거리 모두 구하기
#     #각 치킨집 기준, 집과의 모든 치킨 거리.
#     for i in range(len(chicken)):
#         temp =[]
#         for j in range(len(home)):
#             temp.append(cal_dist(chicken[i], home[j]))
#         dists.append(temp) #순서대로 각 치킨집들의 치킨거리 종류가 다 들어가 있음
    
    