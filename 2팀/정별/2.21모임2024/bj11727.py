n = int(input())
def dp(n):
    dp = [0]* (n+1)
    dp[0] =1
    dp[1] = 3
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]
    
    return dp[n]
        
print(dp(n))