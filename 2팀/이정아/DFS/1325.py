import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
computers = [[] for _ in range(n+1)]
ans = []
maxcnt = 0

for _ in range(m):
    x, y = map(int, input().split())
    computers[y].append(x)

maxCnt, ans = 0, []
for i in range(1, n+1):
    visited = set()
    visited.add(i)
    q = deque([i])
    
    cnt = 0
    
    ## BFS
    while q:
        computer = q.popleft()
        for targetCom in computers[computer]:
            if targetCom not in visited:
                visited.add(targetCom)
                cnt += 1
                q.append(targetCom)
    if cnt > maxCnt:
        maxCnt = cnt
        ans = [i]
    elif cnt == maxCnt:
        ans.append(i)
        
print(*ans)

'''
[DFS] : 한 번에 많이 == 한 번에 깊게. 로 생각해서 DFS로 시도했으나 ,.,
1. 시간초과.. => 2. pypy로 돌리니 recursion error... => 3. limit 올린 후 다시 돌리니 메모리초과..
'''
# def dfs(idx):
#     global cnt, visited
#     for computer in computers[idx]:
#         if computer not in visited:
#             visited.add(computer)
#             cnt += 1
#             dfs(computer)

# for i in range(1, n+1):
#     visited = set() # 처음엔 0 * (n+1)짜리 리스트로 했다 바꿈. 세트는 원소 있나 찾는 데에 O(1)
#     visited.add(i)
#     cnt = 1
#     dfs(i)
#     if maxcnt < cnt:
#         maxcnt = cnt
#         ans = [i]
#     elif maxcnt == cnt:
#         ans.append(i)
