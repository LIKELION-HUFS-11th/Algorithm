n = int(input())
arr = [list(input().strip()) for _ in range(n)]
answer = 0

def check(arr):
    n = len(arr)
    answer = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1

            if cnt > answer:
                answer = cnt

        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > answer:
                answer = cnt

    return answer

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            temp = arr[i][j]
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], temp
            temp_result = check(arr)
            answer = max(answer, temp_result)
            arr[i][j], arr[i][j + 1] = temp, arr[i][j]

        if i + 1 < n:
            temp = arr[i][j]
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], temp
            temp_result = check(arr)
            answer = max(answer, temp_result)
            arr[i][j], arr[i + 1][j] = temp, arr[i][j]

print(answer)

# # 입력
# n = int(input())
# graph = [list(input().strip()) for _ in range(n)]
# # print(graph)

# # 함수
# # 인접한 것과 바꾼 테이블에 대해 가장 긴 연속된 부분 찾기 
# # -> return max_count
# max_count = 0
# def find_longest(graph):
#     global max_count
#     for x in range(n):
#         cnt = 1
#         for y in range(1,n):
#             # 열
#             if graph[x][y] == graph[x][y-1]:
#                 cnt += 1
#             # 만약 같지 않다면 그 상태의 cnt와 max_count를 비교해서 갱신
#             else:
#                 cnt = 1 # cnt는 1로 초기화
#             max_count = max(cnt, max_count)
#         for y in range(1,n):
#             # 행
#             if graph[y][x] == graph[y-1][x]:
#                 cnt += 1
#             else:
#                 cnt = 1 # cnt는 1로 초기화
#             max_count = max(cnt, max_count)
#     return max_count

# # 인접한 두 곳 찾아서 교환
# for x in range(n):
#     for y in range(n):
#         if y+1 < n:
#             # 오른쪽 검사 후 교환
#             if graph[x][y] != graph[x][y+1]:
#                 graph[x][y], graph[x][y+1] = graph[x][y+1], graph[x][y]
#                 temp = find_longest(graph) # 최대 길이 찾기
#                 max_count = max(temp, max_count)
#                 graph[x][y], graph[x][y+1] = graph[x][y+1], graph[x][y] #다시 돌려놓기
#         if x+1 < n:
#             # 아래쪽 검사 후 교환
#             if graph[x][y] != graph[x+1][y]:
#                 graph[x][y], graph[x+1][y] = graph[x+1][y], graph[x][y]
#                 temp = find_longest(graph) # 최대 길이 찾기
#                 max_count = max(temp, max_count)
#                 graph[x][y], graph[x+1][y] = graph[x+1][y], graph[x][y]

# print(max_count)
# # 입력
# n = int(input())
# boxes = [list(input().strip()) for _ in range(n)]
# graph = boxes 
# max_count = 0
# now_candy = 0

# # 틀린 이유: 가로로만 고려해서
# # 함수
# def find_longest_continuous_color():
#     global max_count  
#     global now_candy  
#     # 가로 방향 탐색
#     for x in range(n):
#         left, right = 0, 0  
#         while 0 <= right < n:
#             if graph[x][right] == graph[x][right - 1]:
#                 right += 1
#             else:
#                 now_candy = right - left
#                 max_count_row = max(max_count, now_candy)
#                 left = right
#                 right += 1

#     # 세로 방향 탐색
#     for y in range(n):
#         left, right = 0, 0  
#         while 0 <= right < n:
#             if graph[right][y] == graph[right - 1][y]:
#                 right += 1
#             else:
#                 now_candy = right - left
#                 max_count_col = max(max_count, now_candy)
#                 left = right
#                 right += 1
#     max_count = max(max_count_row, max_count_col)

# dxs = [0, 1, 0, -1]
# dys = [1, 0, -1, 0]

# def in_range(x, y):
#     return x >= 0 and x < n and y >= 0 and y < n

# for x in range(n):
#     for y in range(n):
#         for dx, dy in zip(dxs, dys): 
#             nx, ny = x + dx, y + dy
#             if in_range(nx, ny):
#                 if boxes[x][y] != boxes[nx][ny]:
#                     graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
#                     find_longest_continuous_color()

# print(max_count)