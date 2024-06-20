import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

nList = [[] for _ in range(n+1)]
for _ in range(m):
     a, b = map(int, input().split())
     nList[b].append(a)
     
# print(nList)
# cnt = 0
def bfs(start):
    q=deque()
    q.append(start)
    cnt = 0
    
    visitied = [False] * (n+1)
    visitied[start] = True #일단 방문 표시
    while q:
        nCur = q.popleft() #계속 빼주면서 cnt더하ㅗ고 경우 늘리기
        for next in nList[nCur]:
            if not visitied[next]: #첫방문이면
                visitied[next]=True
                q.append(next) #연결된 애들 넣어주기
                cnt +=1
    return cnt

nAns = []
for start in range(1, len(nList)):
    nAns.append(bfs(start))

for i in range(len(nAns)):
    if max(nAns) == nAns[i]:        
        print(i + 1, end=' ')
