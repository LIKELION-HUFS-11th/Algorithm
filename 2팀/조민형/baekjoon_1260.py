import sys


N, M, V = list(map(int,sys.stdin.readline().split()))
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    vertex_one, vertex_two = list(map(int,sys.stdin.readline().split()))
    graph[vertex_one][vertex_two] = graph[vertex_two][vertex_one] = 1

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

def dfs(V):
    visited1[V] = 1
    print(V, end=" ")
    for i in range(1,N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)    
def bfs(V):
    queue = [V]
    visited2[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end = ' ')
        for i in range(1, N+1):
            if(graph[V][i] == 1 and visited2[i] == 0):
                queue.append(i)
                visited2[i] = 1
                

dfs(V)
print()
bfs(V)

    