import sys
input = sys.stdin.readline

"""
DP
sum/i   0   1   2   ... N
0       1   -   -   ... -   
1       0   1   -   ... -
2       0       1
...
k       0

DP[s][i] = (i를 선택) DP[s-i][i-1] + DP[s][i-1]

i = i를 마지막으로 고름
"""

n, k = map(int, input().split())

DP = [[0 for _ in range(n+1) for _ in range(k+1)]]

for i in range(0, k+1):
    DP[i][i] = 1

for s in range(1, k+1):
    for i in range(1, s):
        DP[s][i] = DP[s-i][i-1] + DP[s][i-1]

total = 0
for i in range(n+1):
    total += DP[k][i]

print(total % 1000000000)
        

