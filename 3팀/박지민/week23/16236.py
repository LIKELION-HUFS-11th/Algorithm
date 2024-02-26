# # 1. 구해야 하는 것
# # 아기 상어가 물고기를 최대로 먹을 때까지 걸리는 시간
# # 2. 먹을 수 있는 조건이 필요할듯
# # 3. 아기상어가 한 칸 이동하는 데 1초 걸림
# # 4. 아기상어 크기 >= 물고기 크기 : 이동 가능
# # 5. 아기상어 크기 > 물고기 크기 : 섭취 가능
# # 6. 아기상어가 이동을 결정하는 방법
# # i) 먹을 게 한 마리면 -> 그거 먹으러 이동
# # ii) 한 마리보다 많으면 -> 최단 거리(이동하는 칸의 최솟값)순, 그리고 가장 왼쪽 위칸을 우선순위로
# # 7. 물고기를 먹으면 빈칸이 됨
# # 8. 자신과 같은 크기의 물고기를 먹으면, 크기 += 1
# # 9. 공간의 상태
# # 물고기 있는 곳: 1 <= <= 6
# from collections import deque
# # 입력
# n = int(input())
# graph = [ list(map(int, input().split())) for _ in range(n)]

# # 상하좌우 이동
# dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

# ## 구현하기 어려웠던 부분
# # 아기상어는 사냥 시 주변에서 가장 가까운 먹이를 탐색하게 되고
# # 거리가 같은 경우 조건대로 움직이게 된다
# # 가까운 먹이를 찾는 탐색 문제이기 때문에 bfs를 생각해볼 수 있음
# # bfs를 사용할 시, 입력: 현재 아기상어의 위치 / 출력: 후보 리스트
# pos = [] # 빈 리스트
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 9:
#             pos.append(i)
#             pos.append(j)

# cnt = 0

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < n

# # 가까운 먹이를 찾는 탐색 문제 -> BFS
# # 아기상어 위치를 기준으로 이동할 후보들 반환
# def bfs(x, y):
#     visited = [[0]*n for _ in range(n)] # 방문체크
#     queue = deque([[x,y]])
#     cand = [] # 후보 리스트

#     visited[x][y] = 1 # 현재 위치 방문처리

#     while queue:
#         i, j = queue.popleft()

#         for idx in range(4):
#             ii, jj = i + dxs[idx], j + dys[idx]
#             # 범위 안에 있고 방문한 적 없다면
#             if in_range(ii, jj) and visited[ii][jj] ==0:
#                 # 현재보다 물고기 크기가 작고 빈 칸이 아니라면
#                 if graph[x][y] > graph[ii][jj] and graph[ii][jj] != 0:
#                     visited[ii][jj] = visited[i][j] + 1
#     # 이동할 때
#     for x in range(n):
#         for y in range(n):
#             for idx in range(4):
#                 nx = x + dxs[idx]
#                 ny = y + dys[idx]
#                 # 아기상어가 물고기보다 크면
#                 if in_range(nx, ny) and height >= graph[nx][ny]: 
#                     # 먹을 수 있는 게 한 마리라면
#                     time += 1 # 이동
#                     graph[x][y] = 0
#                     if height >= graph[nx][ny]: 
#                         graph[x][y] = 0 # 먹으면 빈 칸

# can_eat_cnt = 0
# def can_eat():
#     for x in range(n):
#         for y in range(n):
#             if 0 < graph[x][y] < 9 and graph[x][y] < height:
#                 cnt += 1
#                 cx, cy = x, y
#             if cnt == 1:
#                 return cx, cy
#             # 먹을 게 한 마리가 넘어가면
#             if cnt > 1:
#                 # 최단 거리 골라야 함
#     # 먹는 게 종료되는 시점 : graph에 0이나 9만 있거나 자기랑 크기가 같거나 큰 물고기만 있을 때
#     # 먹을 수 있는 조건
#     if 0 < graph[x][y] < 9 and graph[x][y] < height:
#         bfs()
#     return can_eat_cnt
# 6. 아기상어가 이동을 결정하는 방법
# i) 먹을 게 한 마리면 -> 그거 먹으러 이동
# ii) 한 마리보다 많으면 -> 최단 거리(이동하는 칸의 최솟값)순, 그리고 가장 왼쪽 위칸을 우선순위로
# 7. 물고기를 먹으면 빈칸이 됨


# 언제 먹는 게 종료되나? 
# graph에 0이나 9만 있을 때


# from collections import deque

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)] #공간 정보
# visited= [[0]*n for _ in range(n)] # 방문 처리
# eat_cnt = 0
# time = 0

# length = 2 # 아기상어 크기

# # 시작점 찾기
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 9:
#             baby_x, baby_y = i, j
#             print(baby_x, baby_y)

# dxs = [-1, 1, 0, 0]
# dys = [0, 0, -1, 1]

# def in_range(x,y):
#     return 0 <= x < n and 0 <= y < n

# def bfs(x, y):
#     global time
#     queue = deque()
#     queue.append((x, y))

#     while queue:
#         x, y = queue.popleft()

#         # 아기상어 이동
#         for i in range(4):
#             nx = x + dxs[i]
#             ny = y + dys[i]
#             # 범위 안이고 물고기 있으면서 자기보다 작거나 같은 칸이면 이동
#             if in_range(nx, ny) and graph[nx][ny] != 0:
#                 if graph[nx][ny] <= length:
#                     time += 1 # 이동 시간 1초 소요
#                     graph[x][y] = 0 #원래 자기가 있던 위치 빈칸으로 바꿔쥐기
#                     # 자기보다 작으면 먹기
#                     if graph[nx][ny] < length:
#                         eat_cnt += 1 
#                         graph[nx][ny] = 0 #이미 먹은 곳은 빈칸 됨
#                     # 먹은 물고기 수가 자기 크기와 같아지면 크기 증가
#                     if eat_cnt == length: 
#                         length += 1 # 크기 증가
#                     queue.append((nx, ny))

# for i in range(n):
#     for j in range(n):
#         bfs(baby_x, baby_y)

# print(time)