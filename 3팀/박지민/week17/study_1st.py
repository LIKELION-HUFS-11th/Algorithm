## 입력
n,m = map(int,input().split())
r,c,d = map(int,input().split())
graph =[ list(map(int,input().split())) for _ in range(n) ]
cnt = 0
# 벽이 아니고 청소 안 한 곳이라면 청소 해야 함

## 방문 여부 검사
visited = [[0]*n for _ in range(m)]
## 주변 4칸 검사
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
flag = 0
#북동남서
# 0 1 2 3

# 반시계 방향 회전
def cursion():
    # 북쪽이면 서쪽으로
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    elif d == 3:
        d = 2

def cleaning():
    for r in range(n):
        for c in range(m):
            if graph[r][c] == 0:
                # 벽 아니고 청소 안 했다면
                if visited[r][c] ==0:
                    # 청소하기
                    cnt += 1
                    visited[r][c] = 1 
                    #주변 네 칸 청소했는지 검사하고 
                    for i in range(4):
                        # 하나라도 청소 안 했다면 
                        if 0 <= r+dr[i] < n and 0 <= c + dc[i] < m:
                            if visited[r + dr[i]][c + dc[i]] == 0:
                                flag = 1

if flag == 0:
    # 후진한 곳이 벽이 아니면 후진하고
    r + dr[d]
    c + dr[c]
        
if flag == 1:
    # 반시계방향 회전
    cursion()
    # 청소되지 않은 빈 칸이라면
    if graph[r + dr[d]][c + dc[d]] ==0 and visited[r + dr[d]][c + dc[d]] == 0:
        # 한 칸 전진
        r = r + dr[d]
        c = c + dc[d]
        cleaning()




