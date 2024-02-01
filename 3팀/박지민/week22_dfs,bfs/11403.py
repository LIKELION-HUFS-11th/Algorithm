# 입력
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 함수
def dfs(graph, N, visited, start, end):
    visited[start][end] = 1  # i에서 j로 가는 길이 양수인 경우 1로 표시

    for vertex in range(N):
        if not visited[start][vertex] and graph[start][vertex] == 1:
            dfs(graph, N, visited, vertex, end)

# 결과 출력 위한 2차원 배열
result = [[0] * N for _ in range(N)]

# DFS를 사용하여 i에서 j로 가는 길이 양수인 경우 표시
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:  # i에서 j로 가는 간선이 존재하는 경우
            visited = [[0] * N for _ in range(N)]
            dfs(graph, N, visited, i, j)
            result[i][j] = visited[i][j]

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))
