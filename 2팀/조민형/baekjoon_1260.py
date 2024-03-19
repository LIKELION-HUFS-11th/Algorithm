import sys

N, M, V = list(map(int,sys.stdin.readline().split())) # N은 길이, M은 간선의 수, V는 시작점
graph = [[0]*(N+1) for _ in range(N+1)] # 배열 2차원으로 저장
for _ in range(M): # 두 점을 받고 
    vertex_one, vertex_two = list(map(int,sys.stdin.readline().split())) 
    graph[vertex_one][vertex_two] = graph[vertex_two][vertex_one] = 1 #그래프에서 해당 정점을 양 x,y좌표에 체크표시

visited1 = [0] * (N+1) #방문 그래프 만들기
visited2 = [0] * (N+1) #방문 그래프 만들기

# dfs -> 재귀 사용
def dfs(V):
    visited1[V] = 1
    print(V, end=" ")
    for i in range(1,N+1): #for문 안에서 돌면서 재귀적으로 탐색하여 깊게 들어가며 탐색
        if graph[V][i] == 1 and visited1[i] == 0: 
            dfs(i)

# bfs -> 반복문 사용
def bfs(V):
    queue = [V] #리스트를 queue와 같이 활용, 출발점 넣어놓기
    visited2[V] = 1 # 탐색한 정점을 체크표시
    while queue: # 하나씩 뽑아가면서 갈 경로가 더 없을 때까지 반복
        V = queue.pop(0) #가장 처음의 요소를 빼내어 더 작은 수의 정점부터 탐색하도록
        print(V, end = ' ')
        for i in range(1, N+1):
            if(graph[V][i] == 1 and visited2[i] == 0): # for문을 돌면서 일단 가야 할 경로를 모두 경로 queue에 저장 -> 나중에 하나씩 앞에서 빼가면서 탐색
                queue.append(i)
                visited2[i] = 1
                

dfs(V)
print()
bfs(V)

    