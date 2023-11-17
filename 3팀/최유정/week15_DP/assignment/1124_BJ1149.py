N = int(input())
paint_cost = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = paint_cost[0][0], paint_cost[0][1], paint_cost[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + paint_cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + paint_cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + paint_cost[i][2]

print(min(dp[N-1]))