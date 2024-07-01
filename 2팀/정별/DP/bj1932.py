import sys
# input = sys.stdin.readline
n = int(input())
nTri = [[0] for _ in range(n+2)]
nTri[0] = [0] * (n+2)
# print(nTri)

if n == 1:
    x = int(input())
    print(x)
    
else:
    for i in range(1, n+1): #맨 윗칸과 맨 아랫칸을 0ㅇ으로 비워두자

        nTri[i].extend(list(map(int, sys.stdin.readline().split())))
        nTri[i].extend([0] * (n+1-i))
        
    nTri[-1].extend([0 for _ in range(n+1)])
    # print(nTri)

    dp = nTri

    for i in range(1, n+2):
        for j in range(1, i+1):
            if j == n+1:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1],  dp[i-1][j])
    # print(dp)     
    print(max(dp[-1]))