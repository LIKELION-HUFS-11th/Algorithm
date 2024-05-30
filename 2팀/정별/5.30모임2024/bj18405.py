import sys, heapq
#우선순위 힙 사용.
n, k = map(int, sys.stdin.readline().split())
nLst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, sys.stdin.readline().split())

visited = [[False]*(n) for _ in range(n)]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp[0][0] = nLst[0][0]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

time, virus, heap = 0, [], []

for i in range(n):
    for j in range(n):
        if nLst[i][j]: #비었으면 패스
            num = nLst[i][j]
            heapq.heappush(heap, (num, i, j)) #바이러스 숫자랑 좌표 담기
            visited[i][j] = True

for _ in range(s):
    next_virus = [] #잠깐 담아둘 공간
    while heap:
        now = heapq.heappop(heap) #우선순위큐 통해서 바이러스에 우선순위 부여
        K, I, J = now[0], now[1], now[2] #큐에 담아있던 k번호랑 좌표
        for i in range(4):#4방향 좌표 이동
            nx = I + dx[i] 
            ny = J + dy[i]
            if 0 <= nx <n and 0<= ny <n: #범위안넘어가면
                if not nLst[nx][ny]:
                    nLst[nx][ny] = K #갱신
                    next_virus.append((K, nx, ny)) #새로 넣기
                    #모두 값을 저장해놓았다가 1초가 지나는 시점에
    for v in next_virus: #한번에 queue에 삽입해주는 방식으로 초당 증식
        heapq.heappush(heap, v)
print(nLst[x-1][y-1])

            

