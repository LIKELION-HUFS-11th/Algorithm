import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * n
x = int(input())
dp[0] = x
for i in range(1, n):
    temp = [0] * n
    nums = list(map(int, input().split()))
    nums.extend([0] * (n-1-i))
    for j in range(n):
        if j-1 >= 0:
            temp[j] = max(temp[j], dp[j-1]+nums[j])
        temp[j] = max(temp[j], dp[j]+nums[j])
    dp = temp
print(max(dp))