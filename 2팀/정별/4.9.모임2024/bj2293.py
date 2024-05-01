import sys

n, k = map(int, sys.stdin.readline().split())

nCoins = []
for _ in range(n):
    x = int(sys.stdin.readline())
    nCoins.append(x)

nCoins = sorted(nCoins)

def cnt_coin(coins, target):
    dp = [0] * (target+1) #각 원소는, 해당 인덱스값=가치를 나타낼 수 있는 모든 경우의수 총합
    dp[0]=1
    
    for coin in coins: #현재 동전의 가치가 coin
        for i in range(coin, target+1): # 현재가치가 i
            dp[i] += dp[i - coin] 
#기존의 dp[i]는, 예를들면 coin=2, i=3된 직후,아직 dp[2] = 2, dp[3]=1 임.
#여기서 (coin=1, i=2일때)coin 1원만을 가지고 총합이 2 만드는 경우의 수는 1.
    #(coin=2, i=2일때) dp[2] = dp[2] + dp[2-2] =2
    
#(coin=2, i=3된 직후) coin=1일 때 3원을 만드는 경우의 수 dp[3]=1.
    #coin=2 되고 총합이 3원을 만드는 경우의수는
    # dp[3] = dp[3] + dp[3-2] 이전에 1원만을 가지고 3원을 만든 경우의 수 1은 미리 더함.
    # 여기다가 2원을 새롭게 사용해서 3원을 만들껀데, 가장 큰 coin인 2원 자리는 고정으로 박아두는 것임
    # 그럼 구해야할 가치가 3-2=1 이됨. 그래서 합이 1이되는 경우의 수를 더해주는 것임.

#(coin=2, i=4된 직후)
    #dp[4] = dp[4] + dp[4-2] = 1+dp[2]
    #4를 만들껀데, 일단 이전에 쓴 코인들로 만든 경우의 수들은 미리 더해두고
    #new coin인 2를 원하는 값인 4에 박아두고, 남은 값인 2를 만다는 경우만 추가로 세는 것임
    #이미 dp[2]는 구해졌으니 그대로 더함.

    return dp[target] #모든 코인을 돌고나서 인덱스값=원하는 가치=target의 경우의수 배출

print(cnt_coin(nCoins, k))
