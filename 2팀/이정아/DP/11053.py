n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(1, n):
    maxnum = 0
    # 0 ~ i-1 내에서 가장 긴 증가하는 부분수열 길이 구하기
    for j in range(i):
        if arr[j] < arr[i]:
            maxnum = max(maxnum, dp[j]+1)
    dp[i] = maxnum

print(max(dp) + 1)
        

