# 참고: https://computer-choco.tistory.com/545


n, k = map(int, input().split())
nMod = 1000000000

dp = [[1 for i in range(n+1)] for j in range(k+1)]
#행은 k의 j. 열은 n의 i.

for i in range(2, k+1):
    for j in range(1, n+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % nMod
        
print(dp[k][n])


# dp = [[0] * (n+1) for _ in range(k+1)]
# # print(dp)

# dp[0][0] =1

# for i in range(1, k+1):
#     for j in range(1, n+1):
#         for l in range(1, j+1):
            
#             dp[i][j] += dp[i-1][j-l]
#             dp[i][j] %= nMod
# print(dp)
# print(dp[k][n])



# def count_ways(n, k):

#     dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
#     dp[0][0] = 1 

#     for i in range(1, n+1):
#         for j in range(k+1):
#             dp[i][j] = dp[i-1][j]  # i를 선택하지 않는 경우
#             if j > 0:
#                 dp[i][j] += dp[i][j-1]  # i를 최소 한 번 선택하는 경우
#             dp[i][j] %= MOD

#     return dp[n][k]

# n, k = 6, 4
# print(count_ways(n, k))
  