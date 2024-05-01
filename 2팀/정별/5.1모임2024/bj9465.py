import sys
# T = int(input())

# for _ in range(T):

#     n = int(input())
#     dp= [[0 for _ in range(n)] for _ in range(2)]
    
#     nList = []
#     for _ in range(2):
#         nList.append(list(map(int, sys.stdin.readline().split())))
    
#     for i in range(2):#어차피 2줄
#         for j in range(n):
#             if i==0:
#                 if j ==0:
#                     if nList[i][j] == max(nList[i][j], nList[i+1][j], nList[i][j+1]): #본인제외 2방향에서 최댓값이면
#                         dp[i][j] = nList[i][j]
#                 elif j == n-1:
#                     if nList[i][j] == max(nList[i][j], nList[i+1][j], nList[i][j-1]): #본인제외 2방향에서 최댓값이면
#                         dp[i][j] = nList[i][j]
#                 else:
#                      if nList[i][j] == max(nList[i][j], nList[i+1][j], nList[i][j-1], nList[i][j+1]): #본인제외 3방향에서 최댓값이면
#                         dp[i][j] = nList[i][j]
#             else: #i==1
#                 if j ==0:
#                     if nList[i][j] == max(nList[i][j], nList[i-1][j], nList[i][j+1]): #본인제외 2방향에서 최댓값이면
#                         dp[i][j] = nList[i][j]
#                 elif j == n-1:
#                     if nList[i][j] == max(nList[i][j], nList[i-1][j], nList[i][j-1]): #본인제외 2방향에서 최댓값이면
#                         dp[i][j] = nList[i][j]
                                 
#                 else: #여기서 70이 카운트가 안됨. 삼방에서 가장 큰수가 아니어도, 만약 가장 큰 수가 이미 더 큰 수 옆에 있다면.. 가능!!!
#                     if nList[i][j] == max(nList[i][j], nList[i-1][j], nList[i][j-1], nList[i][j+1]): #본인제외 3방향에서 최댓값이면
#                         dp[i][j] = nList[i][j]
#     cnt = 0
#     for i in range(2):
#         for j in range(n):
#             if dp[i][j]:
#                 cnt += dp[i][j]
#     print(dp)
#     print(cnt)

# 런타임에러
# T = int(input())

# for test_case in range(T):
#     N = int(input())

#     arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

#     arr[0][1] = arr[0][1] + arr[1][0]
#     arr[1][1] = arr[1][1] + arr[0][0]

#     for k in range(2, N):
#         arr[0][k] = arr[0][k] + max(arr[1][k - 1], arr[1][k - 2])
#         arr[1][k] = arr[1][k] + max(arr[0][k - 1], arr[0][k - 2])

#     answer = max(arr[0][N-1], arr[1][N-1])
#     print(answer)

# 스티커
# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

test_cases = int(input())

for _ in range(test_cases):
    stickers_num = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * stickers_num for _ in range(3)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    for n in range(1,stickers_num):
        # 0행의 i번 째 스티커 뜯은 경우
        dp[0][n] = max(dp[1][n-1], dp[2][n-1]) + stickers[0][n]

        # 1행의 i번 째 스티커 뜯은 경우
        dp[1][n] = max(dp[0][n - 1], dp[2][n - 1]) + stickers[1][n]

        # i번 째 열의 스티커를 뜯지 않은 경우
        dp[2][n] = max(dp[0][n-1], dp[1][n-1])

    answer = max(dp[0][-1], dp[1][-1])
    answer = max(answer, dp[2][-1])
    print(answer)