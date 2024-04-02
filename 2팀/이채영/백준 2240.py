
"""
DP
행i = 초
열j = 이동횟수 (w % 2 == 1이면 현위치 = 나무2, w % 2 == 0이면 현위치 = 나무1)
DP[i][j] <- 현재까지 이동횟수가 j(=현위치가 1 or 2일때) i초까지의 자두개수 최대합 저장

초기화
(위치1  2   1)      
i/j|0   1   2        
0  |0   0   0   
1  |0                   
2  |1              
3  |2              
4  |2             
5  |2             
6  |3            
7  |4           

    1   2   1       = where
i/j|0   1   2       drop    
0  |0   0   0   
1  |0               2       
2  |1               1
3  |2               1
4  |2               2
5  |2               2
6  |3               1
7  |4               1


"""

import sys
input = sys.stdin.readline

t, w = map(int, input().split())
tree = [0]

for _ in range(t):
    tree.append(int(input().strip()))

# tree = [0, 2, 1, 1, 2, 2, 1, 1]

"""
초기화
"""
DP = [[0 for _ in range(w+1)] for _ in range(t+1)]

for i in range(1, t+1): #자두 위치가 나무1에서 변하지 않음
    if tree[i] == 2:
        DP[i][0] = DP[i-1][0]
    else:
        DP[i][0] = DP[i-1][0] + 1

"""
DP테이블 채우기
"""
for i in range(1, t+1):
    target = tree[i] #target = 현시점에서 자두를 먹을 수 있는 나무 위치

    for j in range(1, w+1):
        if j % 2 == 0:  #where = 현시점에서 내 위치
            where = 1
        else:
            where = 2
        
        #자두를 먹을 수 있는 위치와 내 현위치  -> 자두를 먹을 수 있는지 확인
        if target == where: #먹음. 따라서 DP[n] = max(가능한 모든 DP[n-1]) + 1!

            # 이때 내가 where에 서 있을 수 있는 경우는 2가지 <- 직전에 이동함 or 직전에 이동하지 않음
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + 1
        
        else: #먹을 수 없음. 따라서 DP[n] = max(가능한 모든 DP[n-1])
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j])
        
print(max(DP[t]))