# DFS 메서드 정의
def dfs(graph, v, visited): #(그래프, 현재 노드, 방문한 노드)
    visited[v] = True # 현재 노드(v) 방문 처리
    print(v, end=" ")
    
    # 현재 노드와 연결된 다른 노드를 재귀적(스택 기반)으로 방문
    for i in graph[v]:
    	if not visited[i]: #방문하지 않은 인접 노드가 있으면
    		dfs(graph, i, visited) #그 인접 노드를 스택에 넣고 방문처리한다
            
# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
	[],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드의 방문 처리를 위한 리스트
visited = [False] * 9

# DFS 함수 호출 (시작 노드: 1)
dfs(graph, 1, visited)
