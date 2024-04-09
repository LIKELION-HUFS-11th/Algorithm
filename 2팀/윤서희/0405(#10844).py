# 1 2 3 4 5 6 7 8 9
import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

answer = sum(dp[n])
print(answer % 1000000000)