import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n개 물건, 버틸 무개 k
dp = [[0] * (k + 1) for _ in range(n + 1)]
infos = [[0, 0]]

for i in range(n):
    info = list(map(int, input().split())) # 무게, 가치
    infos.append(info)

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = infos[i]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

print(dp[n][k])
