from collections import deque

n,k = map(int, input().split())
#바이러스 
virus=[]
#바이러스의 위치 정보(좌표만)
data =[]
for _ in range(n):
    virus.append([list(map(int, input().split())) for _ in range(n)])
target_s, target_x, target_y = map(int, input().split())

#바이러스 종류 출력하는 
def bfs(x,y):
    virus

dx = [1,0,-1,0]
dy = [0,1,0, -1]
#2중 for문 -> 0이 아니면 바이러스 종류와 위치 정보 갱신
for i in range(n):
    for j in range(n):
    #바이러스가 특정 위치에 존재하면 상하좌우로 증식
    if virus[i][j] != 0:
        #위치 정보 갱신
        for k in range(4):
            ex = virus[i][j] + dx[k]
            ey = virus[i][j] + dy[k]
            #바이러스 전파
            virus[ex][ey] = virus[i][j]
            data.append(virus[ex][ey], data[ex][ey]) 

#queue에 바이러스 위치 정보를 넣고
q= deque(data)
#
virus=q.pop()
if data[i][j] == 0:
    q.append(virus, i,j)

#범위 안에 존재하고
if 0<=nx<=n and 0<=ny<=n:
    #바이러스가 없다면
    if virus[i][j] == 0:
        #바이러스 전파
        = virus