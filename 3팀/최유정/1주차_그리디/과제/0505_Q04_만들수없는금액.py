N = int(input())
coins = list(map(int, input().split()))
coins.sort()
result = 1

for c in coins:
    if result < c:
        break
    result += c

print(result)