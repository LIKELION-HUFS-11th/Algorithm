n = int(input())

dp = [[1] * n for _ in range(10)]

for i in range(1, 10):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

ans = 0
for k in range(10):
    ans += dp[k][-1]
print(ans%10007)