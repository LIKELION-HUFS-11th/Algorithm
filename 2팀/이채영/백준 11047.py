# 그리디
import sys
input = sys.stdin.readline

global coins, k

def get_min_coins(i, rest, total):
    global coins, k

    if i > len(coins) - 1 or rest < 0:
        return -1
    
    # if rest == 0:
    #     return total

    coin = coins[i]
    
    cnt = (rest // coin)
    rest -= (cnt * coin)

    total += cnt

    if rest == 0: #바닥조건 위치 여기로 - 반례 있기 때문
        return total

    #이거 return 안넣으면 안됨 조심
    return get_min_coins(i+1, rest, total)


n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input().strip()))

coins.reverse() #가치가 큰 것부터

cnt = get_min_coins(0, k, 0)

print(cnt)


"""
다음 반례 조심
"""
#10 1
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000