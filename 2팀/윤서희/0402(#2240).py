# import sys
# input = sys.stdin.readline

# t, w = map(int, input().split()) # t초, w번
# cnt = 0
# sec = 0

# for i in range(0, t):
#     now = int(input())
#     if sec <= w:
#         if i == 0:
#             before = now
#             continue
#         if now != before:
#             sec += 1
#         cnt += 1
#         before = now
# print(cnt + 1)

import sys
input = sys.stdin.readline

t, w = map(int,input().split()) # 자두 t초 동안 떨어짐, 최대 w번만 움직이고 싶어함
data = [0] + [int(input()) for _ in range(t)] # 자두가 떨어지는 나무의 정보
dp = [[0 for _ in range(w + 1)] for _ in range(t + 1)] # 각각의 시간과 횟수에 따른 최대 자두 수 저장
for i in range(1, t + 1): # 각 시간마다 최대 자두 수 계산
    if data[i] == 1: # 1번 나무에서 자두가 떨어진다면
        dp[i][0] = dp[i - 1][0] + 1
    else: # 2번 나무에서 자두가 떨어진다면
        dp[i][0] = dp[i - 1][0] 
    
    for j in range(1, w + 1): 
        if (data[i] == 1 and j % 2 == 0):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        elif (data[i] == 2 and j % 2 != 0):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
print(max(dp[t]))


    

