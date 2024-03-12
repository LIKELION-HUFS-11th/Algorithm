import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    
dp = [[0]*(n+1) for i in range(n+1)]

for i in range(1, n+1): # 0행 0열은 비움 why? 애초에 인덱스를 0,0부터가 아닌 1,1부터 주므로
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1] # 그래서 0,0부터 시작하는 arr에서는 인덱스 -1 해줘야 함
        
for k in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    
    result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)