#bfs

from collections import deque

m, n = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
# 방향 리스트
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

# queue에 처음에 받은 토마토의 위치 좌표를 append
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1: #토마토 들어있다면
            queue.append([i, j])

# 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
def bfs():
    while queue:
        # 처음 토마토 좌표 x, y 꺼내고
        x, y = queue.popleft()
        # 처음 토마토 사분면의 익힐 토마토들로 이동
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            # 해당 좌표가 좌표 크기를 넘어가면 안됨
            # 그 좌표에 토마토가 익지 않은채로 있어야 함(0)
            
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                # 익히고 1을 더해주면서 횟수 세어주기
                # 여기서 나온 제일 큰 값이 정답
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면
        if j == 0:
            print(-1)
            exit(0) #코드 강제 종료
    # 다 익혔다면 최댓값이 정답
    res = max(res, max(i))
# 처음 시작을 1로 표현
print(res - 1)
