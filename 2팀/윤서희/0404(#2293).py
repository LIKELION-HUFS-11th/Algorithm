'''
[동전 1]
dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

[동전 1, 2]
dp = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

[동전 1, 2, 5]
dp = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10]
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = []

for i in range(n):
    value = int(input())
    values.append(value)

dp = [0] * (k + 1)

dp[0] = 1

for value in values:
    for i in range(value, k + 1):
        dp[i] += dp[i - value]
    print(dp)

print(dp[k])
