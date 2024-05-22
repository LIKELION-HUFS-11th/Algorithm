# 참고사이트: https://sodehdt-ldkt.tistory.com/76
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]
                                                            #???
                                                            

for k in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    
    result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)


# 시간초과
# import sys

# N, M = map(int, sys.stdin.readline().split())

# nTable = []
# for _ in range(N):
#     nTable.append(list(map(int, sys.stdin.readline().split())))


# for _ in range(M):
#     ans = 0
#     Flag = False
    
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     #여기서 풀기
#     x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

#     try:
#         for i in range(x1, x2+1):
#             for j in range(N):
                
#                 if i== x1 and j<y1: #x1줄일때
#                     continue
#                 if i == x2 and y2< j: #x2줄일때 범위 넘어가면
#                     raise NotImplementedError
                
#                 ans += nTable[i][j]
#     except:
#         pass
    
#     print(ans)

