str1 = input()
str2 = input()

len1, len2 = len(str1), len(str2)
dp = [[0] * len1 for _ in range(len2)]
ans = 0

for i in range(len2):
    for j in range(len1):
        if str2[i] == str1[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])
print(ans)
