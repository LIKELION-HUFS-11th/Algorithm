# import sys
# input = sys.stdin.readline

# '''
# 1  1  1
# 3  2  2
# 7  5  5
# 17 12 12
# '''

# n = int(input())
# dp = [[0, 0, 0] for i in range(n + 1)]
# dp[1] = [1, 1, 1]

# for i in range(2, n + 1):
#     dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
#     dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
#     dp[i][2] = dp[i - 1][1] + dp[i - 1][0]

# print(sum(dp[n]) % 9901)

import sys
input = sys.stdin.readline

'''
1  1  1
3  2  2
7  5  5
17 12 12
'''

n = int(input())
dp = [[0, 0, 0] for i in range(n + 1)]
dp[1] = [1, 1, 1]

for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][1] + dp[i - 1][0]) % 9901

print(sum(dp[n]) % 9901)

