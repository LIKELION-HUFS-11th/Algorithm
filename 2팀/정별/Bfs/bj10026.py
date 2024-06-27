from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
sList = [list(input()) for _ in range(n)]
visitied = [[0]*n for _ in range(n)]
ans = [0, 0] #정답 자리
# print(sList)

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visitied[x][y] =1
    
    while q:
        x, y =q.popleft()
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #색깔 동일(현재 위치랑 상화좌우 이동한 자리 색깔), 방문 안한 경우
            if 0<= nx <n and 0 <= ny < n and sList[x][y] ==sList[nx][ny] and not visitied[nx][ny]:
                visitied[nx][ny] =1
                q.append((nx, ny)) #색깔 같은애 자리를 큐에 새로 담기

for i in range(n): #정상인 정답 담기
    for j in range(n):
        if not visitied[i][j]:
            bfs(i, j)
            ans[0] +=1

visitied = [ [0]*n for _ in range(n)]#적록색맹인 기준 재정의
for i in range(n):#아래 for문 2개 합쳐봤는데, 아예 별도로 색깔들 통일부터 해야함
    for j in range(n):
        if sList[i][j] == 'G':
            sList[i][j] = 'R'
    
for i in range(n):
    for j in range(n):
        if not visitied[i][j]:
            bfs(i,j)
            ans[1]+=1

print(ans[0], ans[1])

