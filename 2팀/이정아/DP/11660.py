import sys
input = sys.stdin.readline

'''
DP를 이용한 풀이

[메인 아이디어]
1. dp[a][b] : (0,0) ~ (a,b)까지의 모든 원소를 더한 값
2. dp를 이용해서, 원하는 (x1,y1) ~ (x2,y2)까지의 합을 구하려면 
    dp[x2][y2]에서, 좌측상단 박스와 우측상단 박스를 빼고 중복으로 빼진 부분을 더해주면 됨
'''

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])