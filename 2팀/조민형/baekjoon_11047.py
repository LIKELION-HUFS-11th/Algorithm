import sys

N , K = map(int, sys.stdin.readline().split())

coin_list = []
for _ in range(N):
    coin = int(sys.stdin.readline())
    coin_list.append(coin)
coin_list.reverse()

result = 0
for i in coin_list:
    if K == 0:
        break
    if K//i >= 1:
        result += K//i
        K = K - ((K//i)*i)
print(result)
        

