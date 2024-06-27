import sys
input = sys.stdin.readline

n = int(input())
nList = [0] + list(map(int, input().split()))
print(nList)

dp = [[0 for _ in range(n)] for _ in range(n)]

cnt = 0
nums = n



# for i in range(n,0, -1):
#     if n%i == 0 or n-i > 1:
        

#     if i == n:
#         dp[i] += nList[i]
        
#     dp[i] = nList[n-i] + nList[i]