import sys
limit_number = 150000
sys.setrecursionlimit(limit_number)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

# 최소 시간
time = 0
# 각 칸의 상하좌우를 검사해 매년 줄어들 높이를 기록해두는 함수
height = [[0] * m for _ in range(n)]

# 함수
def dfs(graph):
    global flag, time  
    flag = 0
    while flag == 0:
        for x in range(n):
            for y in range(m):
                if graph[x][y] != 0:
                    # 상하좌우 체크해서 매년 줄어들 높이 갱신하고
                    for index in range(4):
                        dx = x + dxs[index]
                        dy = y + dys[index]
                        # 범위 안에 있고
                        if 0 <= dx < n and 0 <= dy < m:
                            # 상하좌우 중 0의 개수 체크
                            if graph[dx][dy] == 0:
                                height[dx][dy] += 1
                    # 그에 맞게 매년 빙산의 높이 갱신해주기
                    graph[x][y] -= height[x][y]
                time += 1

    ## 한 덩어리가 아니면 dfs 탈출
    ## 상하좌우 중 하나라도 안 접하면 한 덩어리로 본다
def is_one(graph):
    global flag, time
    flag = 0
    for x in range(n):
        for y in range(m):
            for index in range(4):
                dx = x + dxs[index]
                dy = y + dys[index]
                # 그래프를 돌면서 그 칸은 0이 아닌데 상하좌우 다 0이면 걔는 한 덩어리
                if graph[x][y] != 0 and height[dx][dy] >= 2:
                    # 덩어리 개수 하나 증가
                    flag += 1
    dfs(graph)

is_one(graph)

print(time)


# # 입력
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# dxs = [1,-1,0,0]
# dys = [0,0,1,-1]

# # 최소 시간
# time = 0
# # 각 칸의 상하좌우를 검사해 매년 줄어들 높이를 기록해두는 함수
# height = [0*m for _ in range(n)]

# # 함수
# def dfs(graph):
#     global flag
#     while flag == 1:
#         for x in range(n):
#             for y in range(m):
#                 # 상하좌우 체크해서 매년 줄어들 높이 갱신하고
#                 for index in range(4):
#                     dx = x + dxs[index]
#                     dy = y + dys[index]
#                     # 범위 안에 있고
#                     if 0<= dx and dx < n and 0<= dy and dy <= m:
#                         # 상하좌우 중 0의 개수 체크
#                         if graph[dx][dy] == 0:
#                             height[dx][dy] += 1
#                 # 그에 맞게 매년 빙산의 높이 갱신해주기
#                 graph[x][y] -= height[x][y]
#             time += 1

# ## 한 덩어리가 아니면 dfs 탈출
# ## 상하좌우 중 하나라도 안 접하면 한 덩어리로 본다
# def is_one(graph):
#     for x in range(n):
#         for y in range(m):
#             for index in range(4):
#                 dx = x + dxs[index]
#                 dy = y + dys[index]
#                 # 그래프를 돌면서 그 칸은 0이 아닌데 상하좌우 다 0이면 걔는 한 덩어리
#                 if graph[x][y] != 0 and height[dx][dy]==4:
#                     # 덩어리 개수 하나 증가
#                     flag += 1
#                 else:
#                     dfs(graph)

# is_one(graph)

# print(time)
