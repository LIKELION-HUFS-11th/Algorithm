n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(1, n):
    maxnum = 0
    for j in range(i):
        if arr[j] < arr[i]:
            maxnum = max(maxnum, dp[j]+1)
    dp[i] = maxnum

print(max(dp) + 1)
        

