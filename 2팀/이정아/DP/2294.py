import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = set()
for _ in range(n):
    x = int(input())
    coins.add(x)
coins = sorted(list(coins))
# print(coins)
dp = [float('inf')] * (k+1)

for coin in coins:
    for i in range(coin, k+1):
        if i % coin == 0:
            dp[i] = min(dp[i], i//coin)
        dp[i] = min(dp[i], dp[i-coin]+1)
# print(dp)
if dp[-1] != float('inf'):
    print(dp[-1])
else:
    print(-1)