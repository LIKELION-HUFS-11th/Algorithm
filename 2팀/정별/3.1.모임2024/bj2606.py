import sys

def dfs(graph, v, visited): #방문 여부 확인
    visited[v] = True #시작 정점은 바로 지나는거니까 통과로 바꿔준것.
    for i in range(1, len(graph)):
        if graph[v][i] == 1 and not visited[i]:#연결O 방문x
            dfs(graph, i, visited)

nTotalnum = int(input())
nPair = int(input())

# 인접 행렬 생성. 입력된게 1부터라서 다 1 더함.
graph = [[0] * (nTotalnum + 1) for _ in range(nTotalnum + 1)]

for _ in range(nPair):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1 #연결된 것 표시함

# 방문 여부 저장 배열
visited = [False] * (nTotalnum + 1)

# dfs 함수를 통해 1번 컴퓨터에서 시작하여 감염되는 컴퓨터 수 계산
dfs(graph, 1, visited)

count = sum(visited) - 1

print(count)
