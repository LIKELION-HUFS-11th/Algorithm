import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
dx, dy = [0, 1], [1, 0]

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if dp[i][j] > 0:
            for k in range(2):
                if 0<=i+arr[i][j]*dx[k]<n and 0<=j+arr[i][j]*dy[k]<n:
                    # print(dp[i+arr[i][j]*dx[k]][j+arr[i][j]*dy[k]], dp[i][j])
                    dp[i+arr[i][j]*dx[k]][j+arr[i][j]*dy[k]] += dp[i][j]

# print(dp)
print(dp[-1][-1])

        