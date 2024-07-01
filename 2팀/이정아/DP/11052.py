n = int(input())
prices = [0]
prices.extend(list(map(int, input().split())))
    
dp = [0]
dp.extend([prices[1]*i for i in range(1, n+1)])
# print(dp, prices)

for i in range(2, n+1):
    for j in range(i, n+1):
        dp[j] = max(dp[j], dp[j-i]+prices[i])
        # print(i, j, dp)

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         prices[i] = max(prices[i], prices[j]+prices[i-j])

print(prices[-1])