
#n,m 공백으로 입력받기
n,m = map(int,input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
#우, 하, 좌, 상
dy = [0,1,0,-1]
dx = [1,0,-1,0]

#bfs -> 전체 그림의 사이즈(rs)를 구하려는것
#(y,x)부터 시작할 때
def bfs(y,x):
    #(y,x)에 한 개가 있으니까
    rs = 1
    #q에 넣어주고
    q =[(y,x)]
    while q:
        ey,ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            #일단 넘어가는지부터 확인
            if 0<=ny<=n and 0<=nx<=m:
            #새로운 1을 발견할 때마다 rs를 1 증가
                if map[ny][nx] == 1 and chk[ny][nx]==False:
                    chk[ny][nx] = True
                    q.append((ny,nx)) #q에 왜 넣을까?
    return rs


#개수
cnt = 0
#최대값
maxv = 0
#이중for 문
for j in range(n):
    for i in range(m):
        if map[j][i] ==1 and chk[j][i] ==False:
            #방문을 True로 바꿔주고
            chk[j][i] = True
            #전체 그림 개수 +1
            cnt +=1
            #BFS를 통해 그림 크기를 구해주고
            maxv = max(maxv,bfs(j,i))
            #BFS한 결과를 바탕으로 최댓값 갱신

print(cnt)
print(maxv)