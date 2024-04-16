from itertools import combinations

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
homes = []
chickens = []
c_dist = 13**2*13
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            homes.append([i, j])
        elif arr[i][j] == 2:
            chickens.append([i, j])

for c in combinations(chickens, m): # 치킨집 중 m개를 조합으로 추출
    temp = 0
    for h in homes:
        # 한 조합 내의 치킨집 중 가장 짧은, 각 집의 치킨거리 구하기
        dist = 13**2
        for i in range(m):
            dist = min(dist, abs(h[0]-c[i][0])+abs(h[1]-c[i][1]))
        temp += dist
    c_dist = min(c_dist, temp)

print(c_dist)
        


