import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
numbers = [[0] * (N+1)] + [[0] + list(map(int, input().split(" "))) for _ in range(N)]
queries = [list(map(int, input().split(" "))) for _ in range(M)]


def solution(N, M, numbers, queries):
    dp = [[0] * (N+1) for _ in range(N+1)]

    for row in range(1, N+1):
        for col in range(1, N+1):
            dp[row][col] = dp[row][col-1] + dp[row-1][col] + numbers[row][col] - dp[row-1][col-1]

    for query in queries:
        x1, y1, x2, y2 = query
        print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])
    return


solution(N, M, numbers, queries)