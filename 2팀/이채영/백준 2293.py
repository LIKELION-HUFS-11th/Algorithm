import sys
input = sys.stdin.readline



n, k = map(int, input().split())

DP = [0 for _ in range(k + 1)]
DP[0] = 1

coins = []

for _ in range(n):
    coins.append(int(input().strip()))

# coins.sort()


for c in coins:
    for i in range(c, k+1):
        DP[i] += DP[i-c]

print(DP[k])