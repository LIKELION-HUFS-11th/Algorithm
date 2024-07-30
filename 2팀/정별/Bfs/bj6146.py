import sys
from collections import deque

X, Y, n = map(int, sys.stdin.readline().split())
nList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(nList)

nGraph=[[0 for _ in range(1002)] for _ in range(1002)]
#음수도 고려해야한다!!!

for elem in nList:
    nGraph[elem[0]+501][elem[1]+501] = -1 #샘 표시

# cnt = 0
# print(nGraph[501][503])
def bfs(x, y): #매개변수는 출발점 좌표
    queue =deque([[x+501, y+501, 0]])#위치 조정)
    nDir = [(-1,0), (1,0), (0, -1), (0,1)] #좌우하상
    # print(queue)
    
    while queue:
        # nVariables =[]
        # for _ in range(3):
        #     nVariables.append(queue.popleft())
        
        a= queue.popleft()
        
        cur_x, cur_y, dist = a[0], a[1], a[2]
        
        # nLeftqueue= queue.popleft()
        # cur_x, cur_y, dist= nVariables[0], nVariables[1], nVariables[2] 
        if cur_x == X+501 and cur_y == Y+501:
            return dist #지금까지의 거리 반환
        
        for dx, dy in nDir: #좌표 돌기
            next_x, next_y = cur_x + dx, cur_y +dy
            if not nGraph[next_x][next_y] and 0<= next_x < 1002 and 0<= next_y < 1002:
                queue.append([next_x, next_y, dist+1]) #거리 추가
                nGraph[next_x][next_y] = 1 #방문 표시
    return

ans = bfs(0,0)        
print(ans)
    
# nGraph[x][y]+=1 #방문 표시

# if x<=1000: #1001까지 이동 가능= 1001이 +500자리임.
#     if not nGraph[x+1][y]:
#         bfs(x+1, y)

            
    
