# 입력
n = int(input())
coin_list = list(map(int, input().split()))

# 설계
coin_list.sort()
t = 1
for coin in coin_list:
    if t < coin:
        print(t)
        break
    else:
        t += coin