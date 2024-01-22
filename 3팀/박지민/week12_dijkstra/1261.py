## 입력
import sys
input = sys.stdin.readline

m,n = map(int,input().split()) #미로의 가로/세로 길이
data = [] # 미로 정보 저장된 리스트
for _ in range(m):
    data.append(list(map(int,input().split())))
# 방문 체크 리스트
visited = [[0] * m for _ in range(n)]

def dijkstra(start):
    for j in range(m):
        for k in range(n):
            #방문 체크하고
            visited[j][k] = 1
            x, y = j, k
            
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]

            # 상하좌우 돌면서
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # nx, ny가 범위 안에 있다면
                if 0<=nx and nx<m and 0<=ny and ny<n:
                    # 상하좌우 중 하나로만 이동해야 하는데
                    
                    # 다음 위치가 빈방이라면
                    if data[nx][ny] ==0:
                        dijkstra((nx, ny))
                    # 다음 위치가 벽이라면
                    else:
                        # 뿌시고
                        data[nx][ny] = 0

                    

