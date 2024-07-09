import sys
input = sys.stdin.readline

n = int(input())
nList = [0] + list(map(int, input().split()))
# print(nList)

dp = [0]
dp.extend(nList[1]*i for i in range(1, n+1))
# print(dp)

cnt = 0
nums = n

# j는 총 구매할 카드의 수를 의미합니다. i장 이상의 카드를 구매하는 경우를 다룹니다.
# dp[j]는 j장의 카드를 구매할 때의 최대 금액을 의미합니다.
# dp[j - i] + prices[i]는 j - i장의 카드를 구매한 뒤, 
    #   i장의 카드 팩을 추가로 구매했을 때의 금액입니다.

for i in range(1, n+1):
    for j in range(i, n+1):
        dp[j] = max(dp[j], dp[j-i]+nList[i])

print(dp[-1])

# for i in range(n,0, -1):
#     if n%i == 0 or n-i > 1:
        

#     if i == n:
#         dp[i] += nList[i]
        
#     dp[i] = nList[n-i] + nList[i]