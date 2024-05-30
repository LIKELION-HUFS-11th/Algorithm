import sys
input = sys.stdin.readline

"""
이중 for문을 돌면서 시작 지점으로부터 갈 수 있는 곳 + 여기서부터 다시 갈 수 있다면(board값이 0이 아닌 곳)

오른쪽과 하단을 탐색하면서 ch_board를 갱신해준다
"""

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1


for i in range(N):
    for j in range(N):
        if board[i][j] != 0 and dp[i][j] != 0:
            if i + board[i][j] < N:
                dp[i+board[i][j]][j] += dp[i][j]

            if j + board[i][j] < N:
                dp[i][j+board[i][j]] += dp[i][j]

print(dp[-1][-1])