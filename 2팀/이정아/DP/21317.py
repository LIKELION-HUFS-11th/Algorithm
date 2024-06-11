import sys
input = sys.stdin.readline

n = int(input())
energies = []
for _ in range(n-1):
    energies.append(list(map(int, input().split())))

k = int(input())
dp = [[float('inf')] * 2 for _ in range(n)]
dp[0][0] = 0
if n > 1:
    dp[1][0] = energies[0][0]
if n > 2:
    dp[2][0] = min(energies[0][0] + energies[1][0], energies[0][1])

for i in range(3, n):
    dp[i][0] = min(energies[i-1][0] + dp[i-1][0], energies[i-2][1] + dp[i-2][0])
    dp[i][1] = min(min(energies[i-1][0] + dp[i-1][1], energies[i-2][1] + dp[i-2][1]), dp[i-3][0] + k)

print(min(dp[-1][0], dp[-1][1]))
        

