# 만들 수 없는 금액

N = int(input())
coins = list(map(int, input().split()))
coins.sort()
result = 1

for c in coins:
    if result < c:
        break
    result += c

print(result)