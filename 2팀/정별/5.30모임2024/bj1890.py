import sys
#dp
n = int(input())

nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(nums)
#칸 적혀있는 수가 0이상 9이하.

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):#행
    for j in range(n):#열
        if i == n-1 and j == n-1: #다 도착함
            print(dp[i][j])
            break
        cur = nums[i][j] #해당 칸에 적힌 수
        
        if j+ cur <n: #오른쪽으로 이동
            dp[i][j+cur] += dp[i][j] #이동한 자리에 현재 값 더하기
        
        if i+ cur <n:#아래로 이동
            dp[i+cur][j] += dp[i][j]
# print(dp)
            
