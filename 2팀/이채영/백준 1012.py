
####### 예제는 다 맞았는데 런타임에러..ㅠ.ㅜ.

import sys

global dx, dy, M, N, farm, is_visited
dx = [0, 0, 1, -1] #동서남북 순
dy = [1, -1, 0, 0]

def dfs(x, y): #배추를 옮길때마다 재귀함수
    global dx, dy, M, N, farm, is_visited


    can_move = False
    for i in range(4): #동서남북 탐색
        new_x, new_y = x + dx[i], y + dy[i]
        if new_x < 0 or new_x > N - 1 or new_y < 0 or new_y > M - 1:
            continue
        if is_visited[new_x][new_y] == 1: #리스트 범위를 넘거나 이미 방문한 곳이면 패스
            continue
        
        is_visited[new_x][new_y] = 1
        if farm[new_x][new_y] == 1:
            can_move = True
            dfs(new_x, new_y)
    
    if not can_move: #더이상 배추로 이동 불가능하다면
        return





def count_earthworm(): #farm[x][y] = 현재탐색위치
    global dx, dy, M, N, farm, is_visited
    
    cnt_worm = 0

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and is_visited[i][j] == 0:
                cnt_worm += 1
                dfs(i, j)

    return cnt_worm
            


T = int(sys.stdin.readline().strip())

result_list = []
for _ in range(T): #테스트케이스별
    M, N, k = tuple(map(int, sys.stdin.readline().strip().split())) #가로, 세로, 배추위치개수

    farm = [[0 for _ in range(M)] for _ in range(N)] #가로 M, 세로 N인 밭

    is_visited = [[0 for _ in range(M)] for _ in range(N)] #지나가면서 체크했는지 확인할 것

    for _ in range(k):
        X, Y = tuple(map(int, sys.stdin.readline().strip().split()))

        farm[Y][X] = 1

    # 여기까지 초기세팅
        
    result = count_earthworm()

    result_list.append(result)

for elem in result_list:
    print(elem)



