from collections import deque

N, K = map(int, input().split())
coin = deque()
for _ in range(N):
    coin.append(int(input()))
dp = [0] * (max(K, max(coin))+1)

while coin:
    c = coin.popleft()
    dp[c] += 1
    for i in range(c, K+1):
        dp[i] += dp[i-c]

print(dp[K])