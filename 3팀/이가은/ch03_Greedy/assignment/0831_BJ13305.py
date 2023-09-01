'''
[주유소]
https://www.acmicpc.net/problem/13305
'''
n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))
cheapest = 1000000001
result = 0

for i in range(n-1):
    if cheapest > city[i]:
        cheapest = city[i]
    result += cheapest * road[i]

print(result)

