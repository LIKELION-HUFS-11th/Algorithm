import sys
sys.setrecursionlimit(10001)

# 입력
n=int(input())
matrix = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

origin_cnt, special_cnt = 0, 0;

# 적록색약 아닌 사람
def dfs(x,y):
    global origin_cnt
    # 방문 처리
    visited[x][y] = True
    # 현재 컬러
    current_color = matrix[x][y]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def in_range(x,y):
        if 0 <= x and x < n and 0 <= y and y < n:
            return True

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 범위 안에 있고
        if in_range(nx, ny) == True:
            # 방문한 적 없고
            if visited[nx][ny] == False:
                # 현재 색상과 같으면
                if matrix[nx][ny] == current_color:
                    # 방문 처리
                    visited[nx][ny] == True
                    dfs(nx, ny)
                    # 구역 수 1 증가시켜주기
                    # origin_cnt += 1
                    
    
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            origin_cnt += 1

visited = [[False]*n for _ in range(n)]

# 적록색약인 사람
def dfs(x,y):
    global special_cnt
    # G -> R로 바꿔주기
    if matrix[x][y] == 'G':
        matrix[x][y] = 'R'

    # 방문 처리
    visited[x][y] = True
    # 현재 컬러
    current_color = matrix[x][y]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if (0 <= nx < n) and (0 <= ny < n):
            # 방문한 적 없고
            if visited[nx][ny] == False:
                # 현재 색상과 같으면
                if matrix[nx][ny] == current_color:
                    # 방문 처리
                    visited[nx][ny] == True
                    # 구역 수 1 증가시켜주기
                    # special_cnt += 1
                    dfs(nx, ny)
    
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            special_cnt += 1

print(origin_cnt, special_cnt)











