seq1 = input()
seq2 = input()

def lcs(x, y):
    n = len(x)
    m = len(y)
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1): #dp[i][j]는 '처음~i' '처음~j' 간의 LCS 길이임
        for j in range(1, m +1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]

print(lcs(seq1, seq2))