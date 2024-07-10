import sys
sys.setrecursionlimit(10**6)

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [0 for _ in range(n+1)] #답을 여기서 도출

def dfs(x):
    dp[x] = 1 #일단 루트노드 본인도 서브트리에 속함
    for next in graph[x]:
        if not dp[next]:
            dfs(next) #다시 해당 노드의 서브 노드 안으로 들어감
            dp[x] += dp[next]

for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(r)

for _ in range(q):
    x= int(sys.stdin.readline())
    print(dp[x])

# sys.setrecursionlimit(10**4) #재귀의 최대깊이 설정
# n, r, q = map(int, input().split())

# nTree = [[] for _ in range(n+1)] #입력받을 트리
# for _ in range(n-2):
#     u, v = map(int, input().split())
#     nTree[u].append(v)
#     nTree[v].append(u)
# # print(nTree)

# dp = [-1 for _ in range(n+1)]

# def find(node): #루트노드 넣기. 입력받을 u값들
#     dp[node]=1

#     for elem in nTree[node]:
#         if dp[elem] == -1: #아직 방문안했으면
#             dp[node] += find(elem) #다시 그 서브노드 길이 더하는 것임
    
#     return dp[node]

# find(r)       
# sol =[]
# for _ in range(q):
#     u = int(input())
#     sol.append(dp[u])

# for i in range(q):
#     print(sol[i])


