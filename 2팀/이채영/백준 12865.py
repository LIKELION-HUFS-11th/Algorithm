import sys
input = sys.stdin.readline


## 0/1 knapsack 문제

"""
W = [6, 4, 3, 5]
V = [13, 8, 6, 12]
k = 7

DP[i][w] = 최대 용량이 w일 때 0~i번째 짐 중 선택해서 넣을 수 있는 최대 가치 저장
i/w |0   1   2   3   4   5   6   7
0   |0   0   0   0   0   0   13  13     
1   |0
2   |0
3   |0

case1) 현재 짐을 넣음
case2) 현재 짐을 넣지 않음
DP[i][w] = max(DP[i-1][k-w[i]] + v[i], DP[i-1][k])

최종 = DP[n-1][k]

"""
    
    


n, k = map(int, input().split())

W = [] #무게
V = [] #가치

DP = [[0 for _ in range(k + 1)] for _ in range(n)]

for i in range(n):
    w, v = map(int, input().split())

    W.append(w)
    V.append(v)

    if i == 0:
        for j in range(w, k+1): #초기화
            DP[i][j] = v



for i in range(1, n):
    for j in range(1, k+1):
        if W[i] > j: #현재 짐 무게가 남은 무게보다 클 때 : 현재 짐 추가 불가능
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j-W[i]] + V[i], DP[i-1][j])



print(DP[n-1][k])








