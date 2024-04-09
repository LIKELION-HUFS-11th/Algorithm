import sys
input = sys.stdin.readline

n = int(input().strip())
DP = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    DP[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i-1][j+1]
        elif j == 9:
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]

result = 0
for i in range(10):
    result += DP[n][i]

print(result % 1000000000)