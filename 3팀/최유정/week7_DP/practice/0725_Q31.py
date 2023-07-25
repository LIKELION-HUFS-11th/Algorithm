# 금광
# 오른쪽 위, 오른쪽, 오른쪽 아래

def find_max_gold(x, y):
    if (y == m-1):
        return
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<= nx < n and 0<= ny < m):
            dp[nx][ny] = max(dp[nx][ny], dp[x][y]+gold[nx][ny])
            find_max_gold(nx, ny)

test_case = int(input())
dx = [-1, 0, 1]
dy = [1, 1, 1]

for _ in range(test_case):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m)] for _ in range(n)]
    arr = list(map(int, input().split()))
    gold = []
    cnt = 0
    for i in range(n):
        temp = arr[m*i:m*i+m]
        gold.append(temp)
        dp[i][0] = gold[i][0]
    for i in range(n):
        find_max_gold(i, 0)

    max_gold = 0
    for i in range(n):
        max_gold = max(max_gold, dp[i][m-1])
    print(max_gold)