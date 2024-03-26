# import sys

N, M = map(int,input().split())
A = [[] for _ in range(N)]

for i in range(N):
    A[i] = list(map(int,input()))

ans = []

if N >= M:
    size = M
else:
    size = N

i = 0
j = 0

#A는 A[11][10] 크기임 -> 사실은 A[10][9]까지 밖에 없음.
while size > 0:
    
    if A[i][j] == A[i+size-1][j] == A[i][j+size-1] == A[i+size-1][j+size-1]:
        ans.append(size**2)
    
    j += 1
    
    if j+size-1 >= M:
        j = 0
        i += 1
        
    if i+size-1 >= N:
        size -= 1
        i = 0
        j = 0
        
print(max(ans))










# n, m = map(int, sys.stdin.readline().split())

# hitmap = [[]]
# for i in range(n):
#         x = list(sys.stdin.readline())
#         if '\n' in x:
#             x.pop()
#         hitmap.append(x)
# hitmap.pop(0)
# print(hitmap)


# nList = [[0 for _ in range(n)] for _ in range(m)]

# def bfs(v):
#     queue = [v]
#     nList[v]=0
#     while queue:
#         v=queue.pop(0)
        
#         for i in range(1, n+1):
#             if nList[i]==1 and hitmap[v][i]==1:
#                 queue.append(i)
#                 nList[i] = 0
    
    
#     return #최댓값


# ans = 0

# for i in range(m):
#     for k in range(n):
#         point = hitmap[i][k] #4
                
#         if not (point == hitmap[i+1][j] or hitmap[i][j]):
            
            
#         hitmap[i+1][k+1]
        
        
#         ans = max(ans, bfs(point))

# print(ans)
        

